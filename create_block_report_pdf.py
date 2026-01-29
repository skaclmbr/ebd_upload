## library for formatting and saving a pdf block summary

# importing modules
import fpdf
from fpdf import FPDF
from fpdf.outline import TableOfContents
from fpdf.fonts import FontFace
from copy import deepcopy
import json

nl = "\n"
blue = (42, 59, 77)
red = (199,0,57)
ncba_white = (255,255,255)

block_status = ["missing", "COMPLETE"]
block_status_colors = [
    red,
    blue
]

b_cats = [
    "Detected",
    "Possible",
    "Probable",
    "Confirmed"
]

def check_index(my_list, index):
    if 0 <= index < len(my_list):
        return True
    else:
        return False
    

class PDF(FPDF):
    def __init__(self, bsd = {}):
        super().__init__()
        self.link_to_s7_list = self.add_link()
        self.link_to_spp_list = self.add_link()
        self.bsd = deepcopy(bsd)
        self.set_margin(10)
        self.add_page()

        self.print_toc()
        self.print_block_summary()
        self.add_page()
        self.set_link(self.link_to_spp_list)
        self.print_spp_table()
        self.add_page()
        self.set_link(self.link_to_s7_list)
        self.print_s7_table()

    def header(self):
        # Setting font: helvetica bold 15
        self.set_font("helvetica", style="B", size=18)
        self.set_fill_color(42, 59, 77)
        self.set_text_color(255, 255, 255)

        # Printing title:
        self.cell(
            0,
            9,
            self.bsd["ID_NCBA_BLOCK"] + " - " + self.bsd["STATUS"],
            border=0,
            new_x="LMARGIN",
            new_y="NEXT",
            align="L",
            fill=True,
        )
        self.ln(2)
   
        self.set_font("helvetica", size=11)
        self.set_text_color(blue[0], blue[1], blue[2])
        self.cell(
            0,
            8,
            f"Updated {self.bsd['MOST_RECENT_EBD_DATE']}",
            # f"Updated {self.bsd['updateDate']}",
            border = 0,
            align = "L",
            fill = False
        )
        self.ln(10)

    def print_section_heading(self, txt):
        self.ln(5)
        self.set_font("helvetica", style="BI", size = 14)
        self.set_text_color(blue[0], blue[1], blue[2])
        self.cell(
            0, 8, txt, border = 0, align = "L"
        )
        self.ln(10)

    def print_toc(self):
        self.print_section_heading("Contents")
        self.set_font(size = 11)
        self.set_text_color(blue[0],blue[1],blue[2])
        
        line_ht = 5
        self.cell(
            0,
            line_ht,
            "Block Criteria Status"
        )
        self.ln()
        self.cell(
            0,
            line_ht,
            "Species List"
        )
        self.ln()
        self.cell(
            0,
            line_ht,
            "S7 Eligible List"
        )
        self.ln()



    def footer(self):
        # Setting position at 1.5 cm from bottom:
        self.set_y(-15)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", style="I", size=8)
        # Setting text color to gray:
        self.set_text_color(128)
        # Printing page number
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def print_block_summary(self):
        # add block summary stats here.
        # self.start_section(name="Summary Stats", level=0)
        # set up data
        self.print_section_heading("Block Criteria Status")
        status = {
            "breedCountDetected" : {
                "text":"Detected, Uncoded",
                "criteria" : "-",
                "status" : ""},
            "breedCountCoded" : {
                "text" : "Coded",
                "criteria" : ">= 55",
                "status" : "bbcgCoded"
                },
            "breedCountConfirmed" : {
                "text" : "Confirmed",
                "criteria" : ">= 25%",
                "status" : "bbcgConfirmed"
                },
            "breedCountPossible" : {
                "text" : "Possible",
                "criteria" : "<= 25%",
                "status" : "bbcgPossible"
                },
            "breedMinDiurnal" : {
                "text" : "Diurnal Hrs",
                "criteria" : ">= 20",
                "status" : "bbcgTotalEffortHrs"
                },
            "breed1CountDiurnalChecklists" : {
                "text" : "Diurnal Visits (Mar/Apr)",
                "criteria" : ">= 1",
                "status" : ""
                },
            "breed2CountDiurnalChecklists" : {
                "text" : "Diurnal Visits (May/Jun)",
                "criteria" : ">= 1",
                "status" : ""
                },
            "breed3CountDiurnalChecklists" : {
                "text" : "Diurnal Visits (Jul/Aug)",
                "criteria" : ">= 1",
                "status" : ""
                },
            "breedCountNocturnalChecklists" : {
                "text" : "Nocturnal Visits",
                "criteria" : ">= 2 (preferred)",
                "status" : ""
                }
        }


        self.set_fill_color(255,255,255)
        self.set_text_color(42, 59, 77)
        self.set_font("helvetica", size=12)
        with self.table(
            borders_layout = "NONE",
            padding = -1.5,
            col_widths = (40,40,40,40),
            ) as table:

            # headings
            row = table.row()
            for h in ["Statistic", "Value", "Criteria", "Status"]:
                row.cell(h)

            # data
            for type, data in status.items():
                row = table.row()
                row_value = ""
                row_status = ""
                # calculate value
                if type in ["breedCountPossible", "breedCountConfirmed"]:
                    code_type = type[10:]
                    row_value = "{:.1%}".format(
                        self.bsd["breedPct" + code_type]
                    )
                    row_value = row_value + f" ({self.bsd[type]})"
                elif type == "breedMinDiurnal":
                    breedHrs = self.bsd[type]/60
                    row_value = str(f"{breedHrs:.1f}")

                else:
                    row_value = str(self.bsd[type])

                #calculate status
                if data["status"] in self.bsd.keys():
                    # data has boolean complete field
                    row_status = block_status[self.bsd[data["status"]]]
                else:
                    if type[:6] in ["breed1", "breed2", "breed3"]:
                        # calculate breeding season data
                        row_status = block_status[bool(self.bsd[type])]

                row.cell(data["text"])
                row.cell(row_value)
                row.cell(data["criteria"])
                row.cell(row_status)

    def print_spp_table(self):
        # self.start_section(name="Species Table", level=0)
        # Setting font: helvetica 12
        # headings_style = FontFace(
        #     emphasis="BOLD",
        #     color=ncba_white,
        #     fill_color=blue)
        # override_style = FontFace(emphasis="BOLD")

        self.print_section_heading("Species List")
        self.set_font("helvetica", size=12)
        # Setting background color
        self.set_fill_color(42, 59, 77)
        self.set_text_color(255, 255, 255)

        # lists
        spp_list = {
            "Detected" : [],
            "Possible" : [],
            "Probable" : [],
            "Confirmed" : [],
            "s7EligibleChecklists" : []
        }
        # populate lists
        for spp in self.bsd["sppList"]:

            if spp["breedStatus"] in spp_list.keys():
                spp_list[spp["breedStatus"]].append(spp["COMMON_NAME"])
        
        # get the length of the longest list
        table_length = max(
            len(spp_list["Detected"]),
            len(spp_list["Possible"]),
            len(spp_list["Probable"]),
            len(spp_list["Confirmed"]),
        )

        # sort lists alphabetically
        for cat in b_cats: spp_list[cat].sort()

        self.set_fill_color(255,255,255)
        self.set_text_color(42, 59, 77)
        self.set_font("helvetica", size=12)

        with self.table(
            borders_layout = "NONE",
            padding = -1.5,
            col_widths = (30,30,30,30)
            ) as table:
            
            # header rows
            row = table.row()
            # first header row
            for cat in b_cats: row.cell(f"{cat}")
            # second header row
            row = table.row()
            self.set_font("helvetica", style="I", size = 10)
            for cat in b_cats:
                if cat == "Detected":
                    row.cell("")
                else:
                    if cat == "Probable":
                        txt_col = block_status_colors[1]
                    else: 
                        txt_col = block_status_colors[self.bsd["bbcg" + cat]]

                    self.set_text_color(txt_col[0], txt_col[1],txt_col[2])
                    pct = "{:.1%}".format(self.bsd['breedPct' + cat])
                    cnt = f"{self.bsd['breedCount' + cat]}"
                    row.cell(f"{pct} ({cnt})")
            

            # rest of the data
            self.set_font("helvetica", size=9)
            self.set_text_color(blue[0], blue[1], blue[2])
            for i in range(0, table_length):
                row = table.row()
                for cat in b_cats:
                    if not check_index(spp_list[cat], i):
                        row.cell("")
                    else:
                        row.cell(spp_list[cat][i])


    def print_s7_table(self):
        self.print_section_heading("S7 Eligible Species")
        self.set_fill_color(255,255,255)
        self.set_text_color(42, 59, 77)
        self.set_font("helvetica", size=12)
        self.cell(
            0,
            text = "Click on checklist for ebird page and coordinates for directions."
        )
        data = self.bsd["s7EligibleChecklists"]
        # data = self.get_s7_lists()
        # print(data)
        self.ln(10)
        with self.table(
            borders_layout = "NONE",
            padding = 1,
            col_widths = (40,70,100),
            cell_fill_mode="ROWS"
            ) as table:
            # header
            row = table.row()
            for h in ["Checklist", "Coordinates", "Species"]:
                row.cell(h)

            # data
            for sei, info in data.items():
                row = table.row()
                self.set_font("helvetica", size=11, style = "U")
                row.cell(
                    text = sei,
                    link = f'https://ebird.org/checklist/{sei}',
                    v_align = "TOP"
                )
                row.cell(
                    text = f'{info["LATITUDE"]}, {info["LONGITUDE"]}',
                    link = f'https://google.com/maps/search/?api=1&query={info["LATITUDE"]}%2C{info["LONGITUDE"]}',
                    v_align = "TOP"
                )

                self.set_font("helvetica", size=11)
                row.cell(
                    text = "\n".join(info["SPP_LIST"]),
                    v_align = "TOP"
                )
