
# importing modules
from create_block_report_pdf import PDF
from pdf_to_google import upload_file_to_drive
import json


bsd = {
  "_id": "CHAPEL_HILL-SE",
  "ID_NCBA_BLOCK": "CHAPEL_HILL-SE",
  "ID_BLOCK_CODE": "35079H1SE",
  "STATUS": "Complete",
  "updateDate": "2025-05-29",
  "county": "ORANGE",
  "region": "5",
  "breedCountConfirmed": 52,
  "breedCountProbable": 22,
  "breedCountPossible": 30,
  "breedCountCoded": 104,
  "breedCountDetected": 53,
  "breedHrsDiurnal": 923.8356666666665,
  "breedMinNocturnal": 7,
  "breedMinDiurnal": 55430.13999999999,
  "breedHrsNocturnal": 0.11666666666666667,
  "breedPctConfirmed": 0.5,
  "breedPctProbable": 0.21153846153846154,
  "breedPctPossible": 0.28846153846153844,
  "breedCountDiurnalChecklists": 978,
  "breed1CountDiurnalChecklists": 460,
  "breed2CountDiurnalChecklists": 335,
  "breed3CountDiurnalChecklists": 183,
  "breedCountNocturnalChecklists": 3,
  "breed1CountNocturnalChecklists": 2,
  "breed2CountNocturnalChecklists": 1,
  "breed3CountNocturnalChecklists": 0,
  "bbcgCoded": 1,
  "bbcgConfirmed": 1,
  "bbcgPossible": 0,
  "bbcgTotalEffortHrs": 1,
  "bbcgDiurnalVisits": 1,
  "bbcgNocturnalVisits": 1,
  "winterCountDetected": 87,
  "winterMinDiurnal": 23117,
  "winterMinNocturnal": 118,
  "winterHrsDiurnal": 385.28333333333336,
  "winterHrsNocturnal": 1.9666666666666666,
  "winterCountDiurnalChecklists": 372,
  "winter1CountDiurnalChecklists": 179,
  "winter2CountDiurnalChecklists": 193,
  "winterCountNocturnalChecklists": 5,
  "winter1CountNocturnalChecklists": 0,
  "winter2CountNocturnalChecklists": 5,
  "wbcgDetected": 1,
  "wbcgTotalEffortHrs": 1,
  "wbcgDiurnalVisits": 1,
  "wbcgNocturnalVisits": 1,
  "sppList": [
    {
      "COMMON_NAME": "Blue Jay",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Red-bellied Woodpecker",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Red-headed Woodpecker",
      "breedMaxCategory": "C3",
      "breedStatus": "Probable",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Song Sparrow",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Swamp Sparrow",
      "breedMaxCategory": "C3",
      "breedStatus": "Probable",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "White-throated Sparrow",
      "breedMaxCategory": "C3",
      "breedStatus": "Probable",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Carolina Wren",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Northern Flicker",
      "breedMaxCategory": "C2",
      "breedStatus": "Possible",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Red-shouldered Hawk",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "White-breasted Nuthatch",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "American Crow",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "American Goldfinch",
      "breedMaxCategory": "C3",
      "breedStatus": "Probable",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "American Robin",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Black Vulture",
      "breedMaxCategory": "C3",
      "breedStatus": "Probable",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Brown-headed Nuthatch",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Barred Owl",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Brown Thrasher",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Blue-gray Gnatcatcher",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Carolina Chickadee",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Chipping Sparrow",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Common Grackle",
      "breedMaxCategory": "C2",
      "breedStatus": "Possible",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Downy Woodpecker",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Eastern Bluebird",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Eastern Towhee",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Fish Crow",
      "breedMaxCategory": "C2",
      "breedStatus": "Possible",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Hairy Woodpecker",
      "breedMaxCategory": "C3",
      "breedStatus": "Probable",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "House Finch",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Mourning Dove",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Northern Cardinal",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Northern Parula",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Pileated Woodpecker",
      "breedMaxCategory": "C3",
      "breedStatus": "Probable",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Pine Warbler",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Ruby-crowned Kinglet",
      "breedMaxCategory": "C3",
      "breedStatus": "Probable",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Tufted Titmouse",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Turkey Vulture",
      "breedMaxCategory": "C3",
      "breedStatus": "Probable",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "White-eyed Vireo",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Yellow-rumped Warbler",
      "breedMaxCategory": "C2",
      "breedStatus": "Possible",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Yellow-throated Warbler",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Louisiana Waterthrush",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Yellow-bellied Sapsucker",
      "breedMaxCategory": "C2",
      "breedStatus": "Possible",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Dark-eyed Junco",
      "breedMaxCategory": "",
      "breedStatus": "Detected",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Eastern Phoebe",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "European Starling",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Northern Mockingbird",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Brown-headed Cowbird",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Great Blue Heron",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Northern Rough-winged Swallow",
      "breedMaxCategory": "C2",
      "breedStatus": "Possible",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Osprey",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Purple Finch",
      "breedMaxCategory": "C2",
      "breedStatus": "Possible",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Red-tailed Hawk",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Red-winged Blackbird",
      "breedMaxCategory": "C3",
      "breedStatus": "Probable",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Field Sparrow",
      "breedMaxCategory": "C2",
      "breedStatus": "Possible",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Golden-crowned Kinglet",
      "breedMaxCategory": "C2",
      "breedStatus": "Possible",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Mallard",
      "breedMaxCategory": "C3",
      "breedStatus": "Probable",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Coopers Hawk",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Eastern Meadowlark",
      "breedMaxCategory": "",
      "breedStatus": "Detected",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Black-and-white Warbler",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Double-crested Cormorant",
      "breedMaxCategory": "C1",
      "breedStatus": "Detected",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Belted Kingfisher",
      "breedMaxCategory": "C1",
      "breedStatus": "Detected",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Brown Creeper",
      "breedMaxCategory": "",
      "breedStatus": "Detected",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Common Loon",
      "breedMaxCategory": "C1",
      "breedStatus": "Detected",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Hermit Thrush",
      "breedMaxCategory": "C2",
      "breedStatus": "Possible",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Pine Siskin",
      "breedMaxCategory": "C2",
      "breedStatus": "Possible",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Red-breasted Nuthatch",
      "breedMaxCategory": "C2",
      "breedStatus": "Possible",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Wood Duck",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Black-throated Green Warbler",
      "breedMaxCategory": "C2",
      "breedStatus": "Possible",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Common Yellowthroat",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Sharp-shinned Hawk",
      "breedMaxCategory": "",
      "breedStatus": "Detected",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Cedar Waxwing",
      "breedMaxCategory": "C2",
      "breedStatus": "Possible",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Killdeer",
      "breedMaxCategory": "C2",
      "breedStatus": "Possible",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Winter Wren",
      "breedMaxCategory": "C2",
      "breedStatus": "Possible",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Savannah Sparrow",
      "breedMaxCategory": "",
      "breedStatus": "Detected",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Canada Goose",
      "breedMaxCategory": "C3",
      "breedStatus": "Probable",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Chimney Swift",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "American Redstart",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Blue-headed Vireo",
      "breedMaxCategory": "C2",
      "breedStatus": "Possible",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Great Egret",
      "breedMaxCategory": "C1",
      "breedStatus": "Detected",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Ovenbird",
      "breedMaxCategory": "C3",
      "breedStatus": "Probable",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Red-eyed Vireo",
      "breedMaxCategory": "C3",
      "breedStatus": "Probable",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Acadian Flycatcher",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Blackpoll Warbler",
      "breedMaxCategory": "C1",
      "breedStatus": "Detected",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Black-throated Blue Warbler",
      "breedMaxCategory": "C2",
      "breedStatus": "Possible",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Evening Grosbeak",
      "breedMaxCategory": "",
      "breedStatus": "Detected",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Great Crested Flycatcher",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Gray Catbird",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Ruby-throated Hummingbird",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Scarlet Tanager",
      "breedMaxCategory": "C3",
      "breedStatus": "Probable",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Summer Tanager",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Wood Thrush",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Blue Grosbeak",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Eastern Kingbird",
      "breedMaxCategory": "C3",
      "breedStatus": "Probable",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Eastern Wood-Pewee",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "House Wren",
      "breedMaxCategory": "C3",
      "breedStatus": "Probable",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Indigo Bunting",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Northern Waterthrush",
      "breedMaxCategory": "C2",
      "breedStatus": "Possible",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Prairie Warbler",
      "breedMaxCategory": "C2",
      "breedStatus": "Possible",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Prothonotary Warbler",
      "breedMaxCategory": "C3",
      "breedStatus": "Probable",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Rose-breasted Grosbeak",
      "breedMaxCategory": "C2",
      "breedStatus": "Possible",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Worm-eating Warbler",
      "breedMaxCategory": "",
      "breedStatus": "Detected",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Yellow Warbler",
      "breedMaxCategory": "C2",
      "breedStatus": "Possible",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "American Bittern",
      "breedMaxCategory": "",
      "breedStatus": "Detected",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "House Sparrow",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Bald Eagle",
      "breedMaxCategory": "",
      "breedStatus": "Detected",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Hooded Warbler",
      "breedMaxCategory": "C3",
      "breedStatus": "Probable",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Wild Turkey",
      "breedMaxCategory": "C3",
      "breedStatus": "Probable",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Cape May Warbler",
      "breedMaxCategory": "C1",
      "breedStatus": "Detected",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Yellow-throated Vireo",
      "breedMaxCategory": "C3",
      "breedStatus": "Probable",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Palm Warbler",
      "breedMaxCategory": "C2",
      "breedStatus": "Possible",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Gray-cheeked Thrush",
      "breedMaxCategory": "",
      "breedStatus": "Detected",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Veery",
      "breedMaxCategory": "C2",
      "breedStatus": "Possible",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Yellow-billed Cuckoo",
      "breedMaxCategory": "C2",
      "breedStatus": "Possible",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Bay-breasted Warbler",
      "breedMaxCategory": "",
      "breedStatus": "Detected",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Barn Swallow",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Cliff Swallow",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Green Heron",
      "breedMaxCategory": "",
      "breedStatus": "Detected",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Magnolia Warbler",
      "breedMaxCategory": "",
      "breedStatus": "Detected",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Swainsons Thrush",
      "breedMaxCategory": "C2",
      "breedStatus": "Possible",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Mallard (Domestic type)",
      "breedMaxCategory": "",
      "breedStatus": "Detected",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Yellow-breasted Chat",
      "breedMaxCategory": "C2",
      "breedStatus": "Possible",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Chestnut-sided Warbler",
      "breedMaxCategory": "",
      "breedStatus": "Detected",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Broad-winged Hawk",
      "breedMaxCategory": "",
      "breedStatus": "Detected",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Baltimore Oriole",
      "breedMaxCategory": "",
      "breedStatus": "Detected",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Great Horned Owl",
      "breedMaxCategory": "",
      "breedStatus": "Detected",
      "breedDetected": 0,
      "winterDetected": 1,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Tennessee Warbler",
      "breedMaxCategory": "",
      "breedStatus": "Detected",
      "breedDetected": 0,
      "winterDetected": 0,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Pied-billed Grebe",
      "breedMaxCategory": "",
      "breedStatus": "Detected",
      "breedDetected": 0,
      "winterDetected": 1,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Rusty Blackbird",
      "breedMaxCategory": "",
      "breedStatus": "Detected",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Lincolns Sparrow",
      "breedMaxCategory": "",
      "breedStatus": "Detected",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "American Kestrel",
      "breedMaxCategory": "",
      "breedStatus": "Detected",
      "breedDetected": 0,
      "winterDetected": 1,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Common Raven",
      "breedMaxCategory": "",
      "breedStatus": "Detected",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Vesper Sparrow",
      "breedMaxCategory": "",
      "breedStatus": "Detected",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Fox Sparrow",
      "breedMaxCategory": "",
      "breedStatus": "Detected",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Ring-billed Gull",
      "breedMaxCategory": "",
      "breedStatus": "Detected",
      "breedDetected": 0,
      "winterDetected": 1,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "American Woodcock",
      "breedMaxCategory": "C3",
      "breedStatus": "Probable",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Orange-crowned Warbler",
      "breedMaxCategory": "",
      "breedStatus": "Detected",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Rock Pigeon",
      "breedMaxCategory": "C2",
      "breedStatus": "Possible",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Northern Harrier",
      "breedMaxCategory": "",
      "breedStatus": "Detected",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Tree Swallow",
      "breedMaxCategory": "",
      "breedStatus": "Detected",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Ring-necked Pheasant",
      "breedMaxCategory": "",
      "breedStatus": "Detected",
      "breedDetected": 0,
      "winterDetected": 0,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Wilsons Snipe",
      "breedMaxCategory": "",
      "breedStatus": "Detected",
      "breedDetected": 0,
      "winterDetected": 1,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "American Wigeon",
      "breedMaxCategory": "",
      "breedStatus": "Detected",
      "breedDetected": 0,
      "winterDetected": 1,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Northern Shoveler",
      "breedMaxCategory": "",
      "breedStatus": "Detected",
      "breedDetected": 0,
      "winterDetected": 1,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Hooded Merganser",
      "breedMaxCategory": "",
      "breedStatus": "Detected",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Orchard Oriole",
      "breedMaxCategory": "C2",
      "breedStatus": "Possible",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Solitary Sandpiper",
      "breedMaxCategory": "",
      "breedStatus": "Detected",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Blue-winged Warbler",
      "breedMaxCategory": "",
      "breedStatus": "Detected",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Spotted Sandpiper",
      "breedMaxCategory": "",
      "breedStatus": "Detected",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 1,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Sedge Wren",
      "breedMaxCategory": "",
      "breedStatus": "Detected",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "White-crowned Sparrow",
      "breedMaxCategory": "",
      "breedStatus": "Detected",
      "breedDetected": 0,
      "winterDetected": 1,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Purple Martin",
      "breedMaxCategory": "C4",
      "breedStatus": "Confirmed",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Anhinga",
      "breedMaxCategory": "",
      "breedStatus": "Detected",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Marsh Wren",
      "breedMaxCategory": "",
      "breedStatus": "Detected",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Yellow-crowned Night Heron",
      "breedMaxCategory": "",
      "breedStatus": "Detected",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Little Blue Heron",
      "breedMaxCategory": "",
      "breedStatus": "Detected",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Western Cattle Egret",
      "breedMaxCategory": "",
      "breedStatus": "Detected",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Snowy Egret",
      "breedMaxCategory": "",
      "breedStatus": "Detected",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Tricolored Heron",
      "breedMaxCategory": "",
      "breedStatus": "Detected",
      "breedDetected": 1,
      "winterDetected": 0,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    },
    {
      "COMMON_NAME": "Northern House Wren",
      "breedMaxCategory": "C2",
      "breedStatus": "Possible",
      "breedDetected": 1,
      "winterDetected": 1,
      "interimDetected": 0,
      "breedingCodesTxt": "",
      "breedingCodes": [],
      "s7EligibleChecklists": []
    }
  ],
  "ebird_web_data": {
    "_id": "35079H1SE",
    "COUNTY": "ORANGE",
    "ID_BLOCK_CODE": "35079H1SE",
    "ID_EBD_NAME": "Chapel Hill SE",
    "ID_NCBA_BLOCK": "CHAPEL_HILL-SE",
    "REGION": "5",
    "ECOREGION": "P",
    "updateDate": "2025-05-29",
    "breedPctConfirmed": 0.5,
    "breedPctProbable": 0.21153846153846154,
    "breedPctPossible": 0.28846153846153844,
    "bbcgCoded": 1,
    "bbcgConfirmed": 1,
    "bbcgPossible": 0,
    "bbcgTotalEffortHrs": 1,
    "ebird_block_name": "Chapel Hill SE",
    "status": "Complete",
    "priority": 1,
    "diurnal_hrs": 1128.12,
    "nocturnal_hrs": 3.33,
    "num_checklists": 1451,
    "num_atlasers": 141,
    "obs": 53,
    "pos": 30,
    "pro": 22,
    "con": 52,
    "tot": 104,
    "spp": [
      {
        "common_name": "Solitary Sandpiper",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2025-05-08",
        "sampling_event_identifier": "S234798414"
      },
      {
        "common_name": "Gray-cheeked Thrush",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2025-05-08",
        "sampling_event_identifier": "S234798414"
      },
      {
        "common_name": "Hairy Woodpecker",
        "breeding_evidence": "Probable",
        "breeding_code": "P",
        "breeding_category": "C3",
        "recent_location": "104 Channing Ln, Chapel Hill US-NC 35.89289, -79.06202",
        "observation_date": "2025-05-07",
        "sampling_event_identifier": "S240025030"
      },
      {
        "common_name": "Yellow-crowned Night Heron",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2025-05-03",
        "sampling_event_identifier": "S232728622"
      },
      {
        "common_name": "Tree Swallow",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2025-05-03",
        "sampling_event_identifier": "S232728622"
      },
      {
        "common_name": "Blackburnian Warbler",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2025-05-03",
        "sampling_event_identifier": "S232728622"
      },
      {
        "common_name": "Eastern Meadowlark",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "27517, Chapel Hill US-NC 35.87743, -79.02673",
        "observation_date": "2025-05-03",
        "sampling_event_identifier": "S232654649"
      },
      {
        "common_name": "Double-crested Cormorant",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "Few Lake",
        "observation_date": "2025-05-03",
        "sampling_event_identifier": "S232629018"
      },
      {
        "common_name": "European Starling",
        "breeding_evidence": "Confirmed",
        "breeding_code": "NY",
        "breeding_category": "C4",
        "recent_location": "3208 Environ Way, Chapel Hill US-NC 35.90627, -79.02204",
        "observation_date": "2025-05-03",
        "sampling_event_identifier": "S232518261"
      },
      {
        "common_name": "Belted Kingfisher",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "Laurel Hill--CHBC Count Area 21",
        "observation_date": "2025-05-03",
        "sampling_event_identifier": "S232575920"
      },
      {
        "common_name": "Blue-gray Gnatcatcher",
        "breeding_evidence": "Confirmed",
        "breeding_code": "NB",
        "breeding_category": "C4",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2025-04-03",
        "sampling_event_identifier": "S222741597"
      },
      {
        "common_name": "Mallard",
        "breeding_evidence": "Probable",
        "breeding_code": "P",
        "breeding_category": "C3",
        "recent_location": "NC garden Elephant rock trail",
        "observation_date": "2025-03-17",
        "sampling_event_identifier": "S219122505"
      },
      {
        "common_name": "Hooded Merganser",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "The Cedars",
        "observation_date": "2025-03-08",
        "sampling_event_identifier": "S217284311"
      },
      {
        "common_name": "Fox Sparrow",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "Wetlands before Mason Farm ford",
        "observation_date": "2025-03-07",
        "sampling_event_identifier": "S217115823"
      },
      {
        "common_name": "Brown Creeper",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "104 Channing Lane Home Feeder (35.893, -79.062)",
        "observation_date": "2025-02-24",
        "sampling_event_identifier": "S215403765"
      },
      {
        "common_name": "White-crowned Sparrow",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "North Carolina Botanical Garden",
        "observation_date": "2025-02-14",
        "sampling_event_identifier": "S213931769"
      },
      {
        "common_name": "Rusty Blackbird",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2025-01-31",
        "sampling_event_identifier": "S211380880"
      },
      {
        "common_name": "Blackpoll Warbler",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "North Carolina Botanical Garden",
        "observation_date": "2024-10-16",
        "sampling_event_identifier": "S199151881"
      },
      {
        "common_name": "Bay-breasted Warbler",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2024-10-14",
        "sampling_event_identifier": "S198944400"
      },
      {
        "common_name": "Cape May Warbler",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2024-10-05",
        "sampling_event_identifier": "S197620878"
      },
      {
        "common_name": "Great Egret",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "Wetlands before the ford",
        "observation_date": "2024-09-19",
        "sampling_event_identifier": "S195670223"
      },
      {
        "common_name": "Bald Eagle",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "Wetlands before the ford",
        "observation_date": "2024-09-19",
        "sampling_event_identifier": "S195670223"
      },
      {
        "common_name": "Spotted Sandpiper",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "Wetlands before the ford",
        "observation_date": "2024-09-08",
        "sampling_event_identifier": "S195091141"
      },
      {
        "common_name": "Little Blue Heron",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2024-08-07",
        "sampling_event_identifier": "S190608130"
      },
      {
        "common_name": "Yellow-breasted Chat",
        "breeding_evidence": "Possible",
        "breeding_code": "S",
        "breeding_category": "C2",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2024-08-02",
        "sampling_event_identifier": "S189918943"
      },
      {
        "common_name": "Tricolored Heron",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2024-08-01",
        "sampling_event_identifier": "S189893249"
      },
      {
        "common_name": "Snowy Egret",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2024-08-01",
        "sampling_event_identifier": "S189893249"
      },
      {
        "common_name": "Green Heron",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2024-08-01",
        "sampling_event_identifier": "S189893249"
      },
      {
        "common_name": "Western Cattle-Egret",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2024-08-01",
        "sampling_event_identifier": "S189893249"
      },
      {
        "common_name": "Purple Martin",
        "breeding_evidence": "Confirmed",
        "breeding_code": "FY",
        "breeding_category": "C4",
        "recent_location": "Mason Farm Pond",
        "observation_date": "2024-07-03",
        "sampling_event_identifier": "S185149503"
      },
      {
        "common_name": "Chipping Sparrow",
        "breeding_evidence": "Confirmed",
        "breeding_code": "CF",
        "breeding_category": "C4",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2024-06-19",
        "sampling_event_identifier": "S182470537"
      },
      {
        "common_name": "Northern Mockingbird",
        "breeding_evidence": "Confirmed",
        "breeding_code": "CN",
        "breeding_category": "C4",
        "recent_location": "The University of North Carolina at Chapel Hill, Chapel Hill US-NC (35.8983,-79.0412)",
        "observation_date": "2024-05-23",
        "sampling_event_identifier": "S176609924"
      },
      {
        "common_name": "Yellow-billed Cuckoo",
        "breeding_evidence": "Possible",
        "breeding_code": "S",
        "breeding_category": "C2",
        "recent_location": "Piedmont Nature Trail",
        "observation_date": "2024-05-19",
        "sampling_event_identifier": "S175617977"
      },
      {
        "common_name": "Rock Pigeon",
        "breeding_evidence": "Possible",
        "breeding_code": "H",
        "breeding_category": "C2",
        "recent_location": "Kenan Stadium 104 Stadium Drive, Chapel Hill, North Carolina, US (35.907, -79.048)",
        "observation_date": "2024-05-11",
        "sampling_event_identifier": "S173753169"
      },
      {
        "common_name": "Fish Crow",
        "breeding_evidence": "Possible",
        "breeding_code": "H",
        "breeding_category": "C2",
        "recent_location": "Chapel Hill, North Carolina, US (35.911, -79.051)",
        "observation_date": "2024-05-11",
        "sampling_event_identifier": "S173725665"
      },
      {
        "common_name": "Cedar Waxwing",
        "breeding_evidence": "Possible",
        "breeding_code": "H",
        "breeding_category": "C2",
        "recent_location": "Chapel Hill, North Carolina, US (35.911, -79.051)",
        "observation_date": "2024-05-11",
        "sampling_event_identifier": "S173725665"
      },
      {
        "common_name": "Red-bellied Woodpecker",
        "breeding_evidence": "Confirmed",
        "breeding_code": "FY",
        "breeding_category": "C4",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2024-05-11",
        "sampling_event_identifier": "S173473706"
      },
      {
        "common_name": "Prothonotary Warbler",
        "breeding_evidence": "Probable",
        "breeding_code": "S7",
        "breeding_category": "C3",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2024-05-11",
        "sampling_event_identifier": "S173473706"
      },
      {
        "common_name": "Swainson's Thrush",
        "breeding_evidence": "Possible",
        "breeding_code": "S",
        "breeding_category": "C2",
        "recent_location": "The University of North Carolina at Chapel Hill, Chapel Hill US-NC 35.88934, -79.01315",
        "observation_date": "2024-05-08",
        "sampling_event_identifier": "S172835619"
      },
      {
        "common_name": "Indigo Bunting",
        "breeding_evidence": "Confirmed",
        "breeding_code": "CN",
        "breeding_category": "C4",
        "recent_location": "The University of North Carolina at Chapel Hill, Chapel Hill US-NC (35.8818,-79.0133)",
        "observation_date": "2024-05-08",
        "sampling_event_identifier": "S172829211"
      },
      {
        "common_name": "Anhinga",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "Laurel Hill--CHBC Count Area 21",
        "observation_date": "2024-05-04",
        "sampling_event_identifier": "S172029963"
      },
      {
        "common_name": "Marsh Wren",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "Laurel Hill--CHBC Count Area 21",
        "observation_date": "2024-05-04",
        "sampling_event_identifier": "S172035614"
      },
      {
        "common_name": "Field Sparrow",
        "breeding_evidence": "Possible",
        "breeding_code": "S",
        "breeding_category": "C2",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2024-04-18",
        "sampling_event_identifier": "S169199832"
      },
      {
        "common_name": "Ruby-throated Hummingbird",
        "breeding_evidence": "Confirmed",
        "breeding_code": "NB",
        "breeding_category": "C4",
        "recent_location": "104 Channing Lane Home (35.893, -79.062)",
        "observation_date": "2024-04-18",
        "sampling_event_identifier": "S169170665"
      },
      {
        "common_name": "duck sp.",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2024-04-15",
        "sampling_event_identifier": "S168797873"
      },
      {
        "common_name": "Eastern Bluebird",
        "breeding_evidence": "Confirmed",
        "breeding_code": "NY",
        "breeding_category": "C4",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2024-04-15",
        "sampling_event_identifier": "S168797873"
      },
      {
        "common_name": "Lincoln's Sparrow",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2024-04-15",
        "sampling_event_identifier": "S168797873"
      },
      {
        "common_name": "Worm-eating Warbler",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2024-04-15",
        "sampling_event_identifier": "S168797873"
      },
      {
        "common_name": "Tufted Titmouse",
        "breeding_evidence": "Confirmed",
        "breeding_code": "CN",
        "breeding_category": "C4",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2024-04-14",
        "sampling_event_identifier": "S168569590"
      },
      {
        "common_name": "Song Sparrow",
        "breeding_evidence": "Confirmed",
        "breeding_code": "CN",
        "breeding_category": "C4",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2024-04-14",
        "sampling_event_identifier": "S168569590"
      },
      {
        "common_name": "Prairie Warbler",
        "breeding_evidence": "Possible",
        "breeding_code": "S",
        "breeding_category": "C2",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2024-04-14",
        "sampling_event_identifier": "S168569590"
      },
      {
        "common_name": "Northern Parula",
        "breeding_evidence": "Confirmed",
        "breeding_code": "CN",
        "breeding_category": "C4",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2024-04-09",
        "sampling_event_identifier": "S168699371"
      },
      {
        "common_name": "Yellow-rumped Warbler",
        "breeding_evidence": "Possible",
        "breeding_code": "S",
        "breeding_category": "C2",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2024-04-05",
        "sampling_event_identifier": "S167244335"
      },
      {
        "common_name": "Wood Duck",
        "breeding_evidence": "Confirmed",
        "breeding_code": "FL",
        "breeding_category": "C4",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2024-04-03",
        "sampling_event_identifier": "S168055693"
      },
      {
        "common_name": "Osprey",
        "breeding_evidence": "Confirmed",
        "breeding_code": "CF",
        "breeding_category": "C4",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2024-03-31",
        "sampling_event_identifier": "S166636208"
      },
      {
        "common_name": "Savannah Sparrow",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2024-03-31",
        "sampling_event_identifier": "S166630927"
      },
      {
        "common_name": "House Finch",
        "breeding_evidence": "Confirmed",
        "breeding_code": "NB",
        "breeding_category": "C4",
        "recent_location": "Wetlands before Mason Farm ford",
        "observation_date": "2024-03-29",
        "sampling_event_identifier": "S166354138"
      },
      {
        "common_name": "Winter Wren",
        "breeding_evidence": "Possible",
        "breeding_code": "S",
        "breeding_category": "C2",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2024-03-16",
        "sampling_event_identifier": "S165032802"
      },
      {
        "common_name": "American Woodcock",
        "breeding_evidence": "Probable",
        "breeding_code": "C",
        "breeding_category": "C3",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2024-02-19",
        "sampling_event_identifier": "S162301529"
      },
      {
        "common_name": "Buteo sp.",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "UNC Chapel Hill--Hooker Fields",
        "observation_date": "2024-01-27",
        "sampling_event_identifier": "S159966690"
      },
      {
        "common_name": "Great Horned Owl",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2023-12-31",
        "sampling_event_identifier": "S157649256"
      },
      {
        "common_name": "Red-tailed Hawk",
        "breeding_evidence": "Confirmed",
        "breeding_code": "CN",
        "breeding_category": "C4",
        "recent_location": "Chapel Hill atlas",
        "observation_date": "2023-12-24",
        "sampling_event_identifier": "S157109457"
      },
      {
        "common_name": "Sharp-shinned/Cooper's Hawk",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2023-12-21",
        "sampling_event_identifier": "S156805103"
      },
      {
        "common_name": "passerine sp.",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "UNC Chapel Hill--Hooker Fields",
        "observation_date": "2023-11-19",
        "sampling_event_identifier": "S154885495"
      },
      {
        "common_name": "Baltimore Oriole",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2023-09-04",
        "sampling_event_identifier": "S148960757"
      },
      {
        "common_name": "Chestnut-sided Warbler",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2023-09-04",
        "sampling_event_identifier": "S148960757"
      },
      {
        "common_name": "American Golden-Plover",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "Pinehurst Drive",
        "observation_date": "2023-08-31",
        "sampling_event_identifier": "S240352200"
      },
      {
        "common_name": "Eastern Phoebe",
        "breeding_evidence": "Confirmed",
        "breeding_code": "FL",
        "breeding_category": "C4",
        "recent_location": "Baity Hill at Mason Farm",
        "observation_date": "2023-07-31",
        "sampling_event_identifier": "S146115251"
      },
      {
        "common_name": "Barred Owl",
        "breeding_evidence": "Confirmed",
        "breeding_code": "FL",
        "breeding_category": "C4",
        "recent_location": "27517, Chapel Hill US-NC 35.87950, -79.02940",
        "observation_date": "2023-07-06",
        "sampling_event_identifier": "S143768692"
      },
      {
        "common_name": "Acadian Flycatcher",
        "breeding_evidence": "Confirmed",
        "breeding_code": "CF",
        "breeding_category": "C4",
        "recent_location": "The University of North Carolina at Chapel Hill, Chapel Hill US-NC (35.8899,-79.0142)",
        "observation_date": "2023-07-05",
        "sampling_event_identifier": "S146459296"
      },
      {
        "common_name": "Northern House Wren",
        "breeding_evidence": "Probable",
        "breeding_code": "P",
        "breeding_category": "C3",
        "recent_location": "UNC Chapel Hill--Battle Grove",
        "observation_date": "2023-07-02",
        "sampling_event_identifier": "S143349921"
      },
      {
        "common_name": "Cliff Swallow",
        "breeding_evidence": "Confirmed",
        "breeding_code": "FY",
        "breeding_category": "C4",
        "recent_location": "Merritt's Pasture",
        "observation_date": "2023-06-25",
        "sampling_event_identifier": "S142661890"
      },
      {
        "common_name": "hawk sp.",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "The University of North Carolina at Chapel Hill, Chapel Hill US-NC (35.8876,-79.0125)",
        "observation_date": "2023-06-09",
        "sampling_event_identifier": "S140990352"
      },
      {
        "common_name": "Blue Grosbeak",
        "breeding_evidence": "Confirmed",
        "breeding_code": "CF",
        "breeding_category": "C4",
        "recent_location": "The University of North Carolina at Chapel Hill, Chapel Hill US-NC (35.8830,-79.0178)",
        "observation_date": "2023-06-09",
        "sampling_event_identifier": "S140990355"
      },
      {
        "common_name": "Orchard Oriole",
        "breeding_evidence": "Possible",
        "breeding_code": "S",
        "breeding_category": "C2",
        "recent_location": "The University of North Carolina at Chapel Hill, Chapel Hill US-NC 35.89015, -79.01499",
        "observation_date": "2023-06-06",
        "sampling_event_identifier": "S140685199"
      },
      {
        "common_name": "Blue Jay",
        "breeding_evidence": "Confirmed",
        "breeding_code": "FL",
        "breeding_category": "C4",
        "recent_location": "104 Channing Lane Home Feeder (35.893, -79.062)",
        "observation_date": "2023-05-25",
        "sampling_event_identifier": "S139199748"
      },
      {
        "common_name": "Carolina Chickadee",
        "breeding_evidence": "Confirmed",
        "breeding_code": "FY",
        "breeding_category": "C4",
        "recent_location": "Chapel Hill-Pinehurst Dr",
        "observation_date": "2023-05-18",
        "sampling_event_identifier": "S138322335"
      },
      {
        "common_name": "Eastern Kingbird",
        "breeding_evidence": "Probable",
        "breeding_code": "P",
        "breeding_category": "C3",
        "recent_location": "Wetlands before the ford",
        "observation_date": "2023-05-11",
        "sampling_event_identifier": "S137032067"
      },
      {
        "common_name": "Magnolia Warbler",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2023-05-09",
        "sampling_event_identifier": "S136750110"
      },
      {
        "common_name": "Northern Flicker",
        "breeding_evidence": "Possible",
        "breeding_code": "S",
        "breeding_category": "C2",
        "recent_location": "Kings Mill",
        "observation_date": "2023-05-06",
        "sampling_event_identifier": "S136957415"
      },
      {
        "common_name": "Louisiana Waterthrush",
        "breeding_evidence": "Confirmed",
        "breeding_code": "NB",
        "breeding_category": "C4",
        "recent_location": "Kings Mill",
        "observation_date": "2023-05-06",
        "sampling_event_identifier": "S136957415"
      },
      {
        "common_name": "Black-throated Blue Warbler",
        "breeding_evidence": "Possible",
        "breeding_code": "S",
        "breeding_category": "C2",
        "recent_location": "Kings Mill",
        "observation_date": "2023-05-06",
        "sampling_event_identifier": "S136957415"
      },
      {
        "common_name": "Blue-winged Warbler",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2023-05-05",
        "sampling_event_identifier": "S136207839"
      },
      {
        "common_name": "American Redstart",
        "breeding_evidence": "Confirmed",
        "breeding_code": "CN",
        "breeding_category": "C4",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2023-05-05",
        "sampling_event_identifier": "S136207839"
      },
      {
        "common_name": "Yellow Warbler",
        "breeding_evidence": "Possible",
        "breeding_code": "S",
        "breeding_category": "C2",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2023-05-05",
        "sampling_event_identifier": "S136207839"
      },
      {
        "common_name": "Brown Thrasher",
        "breeding_evidence": "Confirmed",
        "breeding_code": "CN",
        "breeding_category": "C4",
        "recent_location": "Baity Hill at Mason Farm",
        "observation_date": "2023-05-03",
        "sampling_event_identifier": "S135912316"
      },
      {
        "common_name": "American Robin",
        "breeding_evidence": "Confirmed",
        "breeding_code": "NY",
        "breeding_category": "C4",
        "recent_location": "Walk from Planetarium, Chapel Hill, North Carolina, US (35.913, -79.052)",
        "observation_date": "2023-04-30",
        "sampling_event_identifier": "S135625082"
      },
      {
        "common_name": "Blue-headed Vireo",
        "breeding_evidence": "Possible",
        "breeding_code": "S",
        "breeding_category": "C2",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2023-04-26",
        "sampling_event_identifier": "S135100959"
      },
      {
        "common_name": "Pine Warbler",
        "breeding_evidence": "Confirmed",
        "breeding_code": "CN",
        "breeding_category": "C4",
        "recent_location": "Parker Preserve",
        "observation_date": "2023-04-23",
        "sampling_event_identifier": "S134731146"
      },
      {
        "common_name": "Sedge Wren",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2023-04-23",
        "sampling_event_identifier": "S134718879"
      },
      {
        "common_name": "Mourning Dove",
        "breeding_evidence": "Confirmed",
        "breeding_code": "NB",
        "breeding_category": "C4",
        "recent_location": "Parker Preserve",
        "observation_date": "2023-04-23",
        "sampling_event_identifier": "S134810858"
      },
      {
        "common_name": "Red-eyed Vireo",
        "breeding_evidence": "Probable",
        "breeding_code": "C",
        "breeding_category": "C3",
        "recent_location": "Parker Preserve",
        "observation_date": "2023-04-23",
        "sampling_event_identifier": "S134810858"
      },
      {
        "common_name": "Eastern Towhee",
        "breeding_evidence": "Confirmed",
        "breeding_code": "CN",
        "breeding_category": "C4",
        "recent_location": "Baity Hill at Mason Farm",
        "observation_date": "2023-04-22",
        "sampling_event_identifier": "S134613439"
      },
      {
        "common_name": "Black-and-white Warbler",
        "breeding_evidence": "Confirmed",
        "breeding_code": "NB",
        "breeding_category": "C4",
        "recent_location": "The University of North Carolina at Chapel Hill, Chapel Hill US-NC 35.88768, -79.01421",
        "observation_date": "2023-04-22",
        "sampling_event_identifier": "S134579562"
      },
      {
        "common_name": "Ovenbird",
        "breeding_evidence": "Probable",
        "breeding_code": "C",
        "breeding_category": "C3",
        "recent_location": "The University of North Carolina at Chapel Hill, Chapel Hill US-NC (35.8855,-79.0181) Parker Preserve",
        "observation_date": "2023-04-21",
        "sampling_event_identifier": "S134492467"
      },
      {
        "common_name": "Yellow-throated Vireo",
        "breeding_evidence": "Probable",
        "breeding_code": "C",
        "breeding_category": "C3",
        "recent_location": "Parker Preserve",
        "observation_date": "2023-04-18",
        "sampling_event_identifier": "S134170465"
      },
      {
        "common_name": "American/Fish Crow",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "The University of North Carolina at Chapel Hill, Chapel Hill US-NC 35.89795, -79.04670",
        "observation_date": "2023-04-14",
        "sampling_event_identifier": "S133712170"
      },
      {
        "common_name": "Common Raven",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "The University of North Carolina at Chapel Hill, Chapel Hill US-NC (35.8823,-79.0126)",
        "observation_date": "2023-04-06",
        "sampling_event_identifier": "S132850222"
      },
      {
        "common_name": "Vesper Sparrow",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2023-04-05",
        "sampling_event_identifier": "S132768887"
      },
      {
        "common_name": "Common Yellowthroat",
        "breeding_evidence": "Confirmed",
        "breeding_code": "CN",
        "breeding_category": "C4",
        "recent_location": "The University of North Carolina at Chapel Hill, Chapel Hill US-NC 35.88485, -79.01267",
        "observation_date": "2023-04-01",
        "sampling_event_identifier": "S132422142"
      },
      {
        "common_name": "Cooper's Hawk",
        "breeding_evidence": "Confirmed",
        "breeding_code": "NB",
        "breeding_category": "C4",
        "recent_location": "UNC Chapel Hill--Battle Park",
        "observation_date": "2023-03-26",
        "sampling_event_identifier": "S131976623"
      },
      {
        "common_name": "American Goldfinch",
        "breeding_evidence": "Probable",
        "breeding_code": "A",
        "breeding_category": "C3",
        "recent_location": "720 Old Mason Farm Road, Chapel Hill, North Carolina, US (35.892, -79.016)",
        "observation_date": "2023-03-26",
        "sampling_event_identifier": "S131845231"
      },
      {
        "common_name": "Pileated Woodpecker",
        "breeding_evidence": "Probable",
        "breeding_code": "P",
        "breeding_category": "C3",
        "recent_location": "720 Old Mason Farm Road, Chapel Hill, North Carolina, US (35.892, -79.016)",
        "observation_date": "2023-03-26",
        "sampling_event_identifier": "S131842160"
      },
      {
        "common_name": "Pine Siskin",
        "breeding_evidence": "Possible",
        "breeding_code": "S",
        "breeding_category": "C2",
        "recent_location": "720 Old Mason Farm Road, Chapel Hill, North Carolina, US (35.892, -79.016)",
        "observation_date": "2023-03-26",
        "sampling_event_identifier": "S131842160"
      },
      {
        "common_name": "Sharp-shinned Hawk",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2023-03-19",
        "sampling_event_identifier": "S131326352"
      },
      {
        "common_name": "American Crow",
        "breeding_evidence": "Confirmed",
        "breeding_code": "CN",
        "breeding_category": "C4",
        "recent_location": "North Carolina Botanical Garden",
        "observation_date": "2023-02-16",
        "sampling_event_identifier": "S128439625"
      },
      {
        "common_name": "American Wigeon",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2023-02-07",
        "sampling_event_identifier": "S127823104"
      },
      {
        "common_name": "White-throated Sparrow",
        "breeding_evidence": "Probable",
        "breeding_code": "T",
        "breeding_category": "C3",
        "recent_location": "104 Channing Ln, Chapel Hill US-NC 35.89288, -79.06202",
        "observation_date": "2023-02-05",
        "sampling_event_identifier": "S127695899"
      },
      {
        "common_name": "Northern Harrier",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2023-01-20",
        "sampling_event_identifier": "S126723378"
      },
      {
        "common_name": "Northern Shoveler",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2023-01-18",
        "sampling_event_identifier": "S126423026"
      },
      {
        "common_name": "Ring-billed Gull",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "Chapel Hill atlas",
        "observation_date": "2022-12-26",
        "sampling_event_identifier": "S124719066"
      },
      {
        "common_name": "Dark-eyed Junco",
        "breeding_evidence": "Possible",
        "breeding_code": "H",
        "breeding_category": "C2",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2022-11-26",
        "sampling_event_identifier": "S123059806"
      },
      {
        "common_name": "Wilson's Snipe",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2022-11-23",
        "sampling_event_identifier": "S122902885"
      },
      {
        "common_name": "Pied-billed Grebe",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "UNC Finley Golf Course, Chapel Hill US-NC 35.89745, -79.02140",
        "observation_date": "2022-11-13",
        "sampling_event_identifier": "S122356901"
      },
      {
        "common_name": "Ring-necked Pheasant",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "201–249 Stancell Dr, Chapel Hill US-NC (35.9028,-79.0016)",
        "observation_date": "2022-10-17",
        "sampling_event_identifier": "S120849745"
      },
      {
        "common_name": "Yellow-bellied Sapsucker",
        "breeding_evidence": "Possible",
        "breeding_code": "H",
        "breeding_category": "C2",
        "recent_location": "104 Channing Ln, Chapel Hill US-NC 35.89286, -79.06209",
        "observation_date": "2022-10-09",
        "sampling_event_identifier": "S120335488"
      },
      {
        "common_name": "Broad-winged Hawk",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "Mt Carmel Church Rd, Chapel Hill US-NC 35.88537, -79.05630",
        "observation_date": "2022-10-07",
        "sampling_event_identifier": "S120148940"
      },
      {
        "common_name": "Wood Thrush",
        "breeding_evidence": "Confirmed",
        "breeding_code": "CF",
        "breeding_category": "C4",
        "recent_location": "The University of North Carolina at Chapel Hill, Chapel Hill US-NC 35.89015, -79.01499",
        "observation_date": "2022-07-06",
        "sampling_event_identifier": "S114524723"
      },
      {
        "common_name": "Eastern Wood-Pewee",
        "breeding_evidence": "Confirmed",
        "breeding_code": "FY",
        "breeding_category": "C4",
        "recent_location": "The University of North Carolina at Chapel Hill, Chapel Hill US-NC 35.88328, -79.01817",
        "observation_date": "2022-06-28",
        "sampling_event_identifier": "S113964787"
      },
      {
        "common_name": "Brown-headed Cowbird",
        "breeding_evidence": "Confirmed",
        "breeding_code": "FL",
        "breeding_category": "C4",
        "recent_location": "Kings Mill",
        "observation_date": "2022-06-25",
        "sampling_event_identifier": "S113745506"
      },
      {
        "common_name": "Northern Cardinal",
        "breeding_evidence": "Confirmed",
        "breeding_code": "NY",
        "breeding_category": "C4",
        "recent_location": "North Carolina Botanical Garden",
        "observation_date": "2022-06-23",
        "sampling_event_identifier": "S113606170"
      },
      {
        "common_name": "crow sp.",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "Wilson-Mitchell Courtyard",
        "observation_date": "2022-06-07",
        "sampling_event_identifier": "S112386783"
      },
      {
        "common_name": "Northern Rough-winged Swallow",
        "breeding_evidence": "Possible",
        "breeding_code": "H",
        "breeding_category": "C2",
        "recent_location": "The University of North Carolina at Chapel Hill, Chapel Hill US-NC 35.90689, -79.03630",
        "observation_date": "2022-05-21",
        "sampling_event_identifier": "S110849493"
      },
      {
        "common_name": "swallow sp.",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "The University of North Carolina at Chapel Hill, Chapel Hill US-NC 35.90689, -79.03630",
        "observation_date": "2022-05-21",
        "sampling_event_identifier": "S110849493"
      },
      {
        "common_name": "White-breasted Nuthatch",
        "breeding_evidence": "Confirmed",
        "breeding_code": "FL",
        "breeding_category": "C4",
        "recent_location": "The University of North Carolina at Chapel Hill, Chapel Hill US-NC (35.9082,-79.0315)",
        "observation_date": "2022-05-19",
        "sampling_event_identifier": "S110737785"
      },
      {
        "common_name": "Northern Waterthrush",
        "breeding_evidence": "Possible",
        "breeding_code": "S",
        "breeding_category": "C2",
        "recent_location": "The University of North Carolina at Chapel Hill, Chapel Hill US-NC 35.89240, -79.01644",
        "observation_date": "2022-05-08",
        "sampling_event_identifier": "S109591458"
      },
      {
        "common_name": "Killdeer",
        "breeding_evidence": "Possible",
        "breeding_code": "S",
        "breeding_category": "C2",
        "recent_location": "Glennwood",
        "observation_date": "2022-05-03",
        "sampling_event_identifier": "S108849485"
      },
      {
        "common_name": "Hooded Warbler",
        "breeding_evidence": "Probable",
        "breeding_code": "T",
        "breeding_category": "C3",
        "recent_location": "Glennwood",
        "observation_date": "2022-05-03",
        "sampling_event_identifier": "S108849485"
      },
      {
        "common_name": "Barn Swallow",
        "breeding_evidence": "Confirmed",
        "breeding_code": "ON",
        "breeding_category": "C4",
        "recent_location": "Merritt's Pasture",
        "observation_date": "2022-05-03",
        "sampling_event_identifier": "S108848169"
      },
      {
        "common_name": "Gray Catbird",
        "breeding_evidence": "Confirmed",
        "breeding_code": "CN",
        "breeding_category": "C4",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2022-05-02",
        "sampling_event_identifier": "S108731045"
      },
      {
        "common_name": "Swamp Sparrow",
        "breeding_evidence": "Probable",
        "breeding_code": "A",
        "breeding_category": "C3",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2022-05-02",
        "sampling_event_identifier": "S108731045"
      },
      {
        "common_name": "Louisiana/Northern Waterthrush",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2022-05-02",
        "sampling_event_identifier": "S108731045"
      },
      {
        "common_name": "Scarlet Tanager",
        "breeding_evidence": "Probable",
        "breeding_code": "T",
        "breeding_category": "C3",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2022-05-02",
        "sampling_event_identifier": "S108731045"
      },
      {
        "common_name": "Wild Turkey",
        "breeding_evidence": "Probable",
        "breeding_code": "C",
        "breeding_category": "C3",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2022-05-02",
        "sampling_event_identifier": "S108704912"
      },
      {
        "common_name": "Red-shouldered Hawk",
        "breeding_evidence": "Confirmed",
        "breeding_code": "CF",
        "breeding_category": "C4",
        "recent_location": "The University of North Carolina at Chapel Hill, Chapel Hill US-NC 35.89503, -79.02195",
        "observation_date": "2022-04-30",
        "sampling_event_identifier": "S108547164"
      },
      {
        "common_name": "Red-winged Blackbird",
        "breeding_evidence": "Probable",
        "breeding_code": "P",
        "breeding_category": "C3",
        "recent_location": "The University of North Carolina at Chapel Hill, Chapel Hill US-NC 35.89503, -79.02195",
        "observation_date": "2022-04-30",
        "sampling_event_identifier": "S108547164"
      },
      {
        "common_name": "Chimney Swift",
        "breeding_evidence": "Confirmed",
        "breeding_code": "ON",
        "breeding_category": "C4",
        "recent_location": "Cosmic Cantina, Chapel Hill",
        "observation_date": "2022-04-27",
        "sampling_event_identifier": "S108258985"
      },
      {
        "common_name": "finch sp.",
        "breeding_evidence": "Possible",
        "breeding_code": "H",
        "breeding_category": "C2",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2022-04-23",
        "sampling_event_identifier": "S107806947"
      },
      {
        "common_name": "Orange-crowned Warbler",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2022-04-05",
        "sampling_event_identifier": "S106335739"
      },
      {
        "common_name": "Hermit Thrush",
        "breeding_evidence": "Possible",
        "breeding_code": "S",
        "breeding_category": "C2",
        "recent_location": "The University of North Carolina at Chapel Hill, Chapel Hill US-NC 35.89345, -79.01813",
        "observation_date": "2022-04-04",
        "sampling_event_identifier": "S106261976"
      },
      {
        "common_name": "Red-headed Woodpecker",
        "breeding_evidence": "Probable",
        "breeding_code": "N",
        "breeding_category": "C3",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2022-03-26",
        "sampling_event_identifier": "S105602765"
      },
      {
        "common_name": "Black Vulture",
        "breeding_evidence": "Probable",
        "breeding_code": "C",
        "breeding_category": "C3",
        "recent_location": "Baity Hill at Mason Farm",
        "observation_date": "2022-03-11",
        "sampling_event_identifier": "S104623003"
      },
      {
        "common_name": "Golden-crowned Kinglet",
        "breeding_evidence": "Possible",
        "breeding_code": "H",
        "breeding_category": "C2",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2022-03-05",
        "sampling_event_identifier": "S104224745"
      },
      {
        "common_name": "Common Grackle",
        "breeding_evidence": "Possible",
        "breeding_code": "S",
        "breeding_category": "C2",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2022-03-05",
        "sampling_event_identifier": "S104214226"
      },
      {
        "common_name": "Brown-headed Nuthatch",
        "breeding_evidence": "Confirmed",
        "breeding_code": "NB",
        "breeding_category": "C4",
        "recent_location": "Chapel Hill-Pinehurst Dr",
        "observation_date": "2022-02-02",
        "sampling_event_identifier": "S101900796"
      },
      {
        "common_name": "American Kestrel",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2021-12-29",
        "sampling_event_identifier": "S99623173"
      },
      {
        "common_name": "Tennessee Warbler",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2021-09-05",
        "sampling_event_identifier": "S94234025"
      },
      {
        "common_name": "Empidonax sp.",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2021-09-01",
        "sampling_event_identifier": "S94030054"
      },
      {
        "common_name": "White-eyed Vireo",
        "breeding_evidence": "Confirmed",
        "breeding_code": "FL",
        "breeding_category": "C4",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2021-06-25",
        "sampling_event_identifier": "S90775324"
      },
      {
        "common_name": "Great Crested Flycatcher",
        "breeding_evidence": "Confirmed",
        "breeding_code": "CN",
        "breeding_category": "C4",
        "recent_location": "Baity Hill at Mason Farm",
        "observation_date": "2021-06-18",
        "sampling_event_identifier": "S90383308"
      },
      {
        "common_name": "Summer Tanager",
        "breeding_evidence": "Confirmed",
        "breeding_code": "CN",
        "breeding_category": "C4",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2021-05-23",
        "sampling_event_identifier": "S89360086"
      },
      {
        "common_name": "Veery",
        "breeding_evidence": "Possible",
        "breeding_code": "S",
        "breeding_category": "C2",
        "recent_location": "The University of North Carolina at Chapel Hill, Chapel Hill US-NC 35.88923, -79.01280",
        "observation_date": "2021-05-20",
        "sampling_event_identifier": "S88590994"
      },
      {
        "common_name": "Carolina Wren",
        "breeding_evidence": "Confirmed",
        "breeding_code": "NY",
        "breeding_category": "C4",
        "recent_location": "North Carolina Botanical Garden",
        "observation_date": "2021-05-14",
        "sampling_event_identifier": "S88084724"
      },
      {
        "common_name": "Great Blue Heron",
        "breeding_evidence": "Confirmed",
        "breeding_code": "ON",
        "breeding_category": "C4",
        "recent_location": "Laurel Hill--CHBC Count Area 21",
        "observation_date": "2021-05-08",
        "sampling_event_identifier": "S87539922"
      },
      {
        "common_name": "Downy Woodpecker",
        "breeding_evidence": "Confirmed",
        "breeding_code": "NY",
        "breeding_category": "C4",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2021-05-06",
        "sampling_event_identifier": "S87234996"
      },
      {
        "common_name": "new world warbler sp.",
        "breeding_evidence": "Possible",
        "breeding_code": "S",
        "breeding_category": "C2",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2021-04-30",
        "sampling_event_identifier": "S86719232"
      },
      {
        "common_name": "Rose-breasted Grosbeak",
        "breeding_evidence": "Possible",
        "breeding_code": "S",
        "breeding_category": "C2",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2021-04-30",
        "sampling_event_identifier": "S86719232"
      },
      {
        "common_name": "Canada Goose",
        "breeding_evidence": "Probable",
        "breeding_code": "P",
        "breeding_category": "C3",
        "recent_location": "Mason Farm Pond",
        "observation_date": "2021-04-30",
        "sampling_event_identifier": "S86705997"
      },
      {
        "common_name": "Evening Grosbeak",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "Parker Preserve",
        "observation_date": "2021-04-29",
        "sampling_event_identifier": "S86634875"
      },
      {
        "common_name": "House Sparrow",
        "breeding_evidence": "Confirmed",
        "breeding_code": "CF",
        "breeding_category": "C4",
        "recent_location": "2160 Environ Way, Chapel Hill US-NC 35.90724, -79.02282",
        "observation_date": "2021-04-28",
        "sampling_event_identifier": "S86552874"
      },
      {
        "common_name": "Palm Warbler",
        "breeding_evidence": "Possible",
        "breeding_code": "H",
        "breeding_category": "C2",
        "recent_location": "The University of North Carolina at Chapel Hill, Chapel Hill US-NC 35.89287, -79.01483",
        "observation_date": "2021-04-13",
        "sampling_event_identifier": "S85573447"
      },
      {
        "common_name": "Black-throated Green Warbler",
        "breeding_evidence": "Possible",
        "breeding_code": "S",
        "breeding_category": "C2",
        "recent_location": "The University of North Carolina at Chapel Hill, Chapel Hill US-NC 35.89287, -79.01483",
        "observation_date": "2021-04-13",
        "sampling_event_identifier": "S85573447"
      },
      {
        "common_name": "American Bittern",
        "breeding_evidence": "Observed",
        "breeding_category": "C1",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2021-04-11",
        "sampling_event_identifier": "S85323990"
      },
      {
        "common_name": "Turkey Vulture",
        "breeding_evidence": "Probable",
        "breeding_code": "C",
        "breeding_category": "C3",
        "recent_location": "UNC Chapel Hill--Coker Arboretum",
        "observation_date": "2021-04-04",
        "sampling_event_identifier": "S84805069"
      },
      {
        "common_name": "Red-breasted Nuthatch",
        "breeding_evidence": "Possible",
        "breeding_code": "S",
        "breeding_category": "C2",
        "recent_location": "Parker Preserve",
        "observation_date": "2021-04-01",
        "sampling_event_identifier": "S84542014"
      },
      {
        "common_name": "Yellow-throated Warbler",
        "breeding_evidence": "Confirmed",
        "breeding_code": "CN",
        "breeding_category": "C4",
        "recent_location": "Mason Farm Biological Reserve",
        "observation_date": "2021-04-01",
        "sampling_event_identifier": "S84534978"
      },
      {
        "common_name": "Common Loon",
        "breeding_evidence": "Observed",
        "breeding_code": "F",
        "breeding_category": "C1",
        "recent_location": "Little Creek Trail",
        "observation_date": "2021-03-30",
        "sampling_event_identifier": "S84417956"
      },
      {
        "common_name": "Ruby-crowned Kinglet",
        "breeding_evidence": "Probable",
        "breeding_code": "M",
        "breeding_category": "C3",
        "recent_location": "Little Creek Trail",
        "observation_date": "2021-03-30",
        "sampling_event_identifier": "S84417956"
      },
      {
        "common_name": "Purple Finch",
        "breeding_evidence": "Possible",
        "breeding_code": "S",
        "breeding_category": "C2",
        "recent_location": "Little Creek Trail",
        "observation_date": "2021-03-30",
        "sampling_event_identifier": "S84417956"
      }
    ],
    "top_atlasers": [
      {
        "rank": 1,
        "observer": "Jin Bai",
        "confirmed-species": 25
      },
      {
        "rank": 2,
        "observer": "Nan Dewire",
        "confirmed-species": 24
      },
      {
        "rank": 3,
        "observer": "Loren Hintz",
        "confirmed-species": 15
      },
      {
        "rank": 4,
        "observer": "Cathy Rodrigues",
        "confirmed-species": 13
      },
      {
        "rank": 5,
        "observer": "Margaret Vimmerstedt",
        "confirmed-species": 11
      },
      {
        "rank": 5,
        "observer": "Fleeta Chauvigne",
        "confirmed-species": 11
      },
      {
        "rank": 7,
        "observer": "Zane Fish",
        "confirmed-species": 10
      },
      {
        "rank": 8,
        "observer": "Roger Shaw",
        "confirmed-species": 8
      },
      {
        "rank": 8,
        "observer": "Alex Nickley",
        "confirmed-species": 8
      },
      {
        "rank": 10,
        "observer": "Nathaniel Blackford",
        "confirmed-species": 6
      },
      {
        "rank": 10,
        "observer": "Emma Blackford",
        "confirmed-species": 6
      },
      {
        "rank": 12,
        "observer": "Curtis Brooks",
        "confirmed-species": 5
      },
      {
        "rank": 13,
        "observer": "Allen Hurlbert",
        "confirmed-species": 4
      },
      {
        "rank": 13,
        "observer": "Margaret Viens",
        "confirmed-species": 4
      },
      {
        "rank": 13,
        "observer": "Suzanne Roberts",
        "confirmed-species": 4
      },
      {
        "rank": 16,
        "observer": "Martin Wall",
        "confirmed-species": 3
      },
      {
        "rank": 17,
        "observer": "Rebekkah LaBlue",
        "confirmed-species": 2
      },
      {
        "rank": 17,
        "observer": "Heather Russell",
        "confirmed-species": 2
      },
      {
        "rank": 17,
        "observer": "Allen Boynton",
        "confirmed-species": 2
      },
      {
        "rank": 17,
        "observer": "Evans Lodge",
        "confirmed-species": 2
      },
      {
        "rank": 17,
        "observer": "Karen Avants",
        "confirmed-species": 2
      },
      {
        "rank": 17,
        "observer": "Ben Nickley",
        "confirmed-species": 2
      },
      {
        "rank": 17,
        "observer": "Ash Ranson",
        "confirmed-species": 2
      },
      {
        "rank": 17,
        "observer": "Nathan Tarr",
        "confirmed-species": 2
      },
      {
        "rank": 17,
        "observer": "Marcia Mandel",
        "confirmed-species": 2
      },
      {
        "rank": 17,
        "observer": "Jeremy Wrenn",
        "confirmed-species": 2
      },
      {
        "rank": 17,
        "observer": "Ron Martin",
        "confirmed-species": 2
      },
      {
        "rank": 28,
        "observer": "don pelly",
        "confirmed-species": 1
      },
      {
        "rank": 28,
        "observer": "Angie  Holt",
        "confirmed-species": 1
      },
      {
        "rank": 28,
        "observer": "Sam Finnegan",
        "confirmed-species": 1
      },
      {
        "rank": 28,
        "observer": "Kathy Richardson",
        "confirmed-species": 1
      },
      {
        "rank": 28,
        "observer": "Melanie Crawford",
        "confirmed-species": 1
      },
      {
        "rank": 28,
        "observer": "Mary Abrams",
        "confirmed-species": 1
      },
      {
        "rank": 28,
        "observer": "Paul Dayer",
        "confirmed-species": 1
      },
      {
        "rank": 28,
        "observer": "steve b",
        "confirmed-species": 1
      },
      {
        "rank": 28,
        "observer": "LEN OToole",
        "confirmed-species": 1
      },
      {
        "rank": 28,
        "observer": "cheryl kegg",
        "confirmed-species": 1
      },
      {
        "rank": 28,
        "observer": "Mel Green",
        "confirmed-species": 1
      },
      {
        "rank": 28,
        "observer": "Mark Rodrigues",
        "confirmed-species": 1
      },
      {
        "rank": 28,
        "observer": "Bryan Sharp",
        "confirmed-species": 1
      },
      {
        "rank": 28,
        "observer": "Scott Anderson",
        "confirmed-species": 1
      },
      {
        "rank": 28,
        "observer": "Morgan Freese",
        "confirmed-species": 1
      },
      {
        "rank": 28,
        "observer": "Ian Wrenn",
        "confirmed-species": 1
      },
      {
        "rank": 28,
        "observer": "Lincoln Martin",
        "confirmed-species": 1
      },
      {
        "rank": 28,
        "observer": "Jeffrey Blalock",
        "confirmed-species": 1
      }
    ],
    "recent_visits": [
      {
        "observer": "Cathy Rodrigues",
        "observation_date": "2025-05-21",
        "checklist": "S240964431",
        "observation_start_time": "12:33",
        "recent_location": "104 Channing Ln, Chapel Hill US-NC 35.89287, -79.06205, Orange",
        "num_spp": 13
      },
      {
        "observer": "Cathy Rodrigues",
        "observation_date": "2025-05-18",
        "checklist": "S240025009",
        "observation_start_time": "10:41",
        "recent_location": "104 Channing Ln, Chapel Hill US-NC 35.89287, -79.06205, Orange",
        "num_spp": 13
      },
      {
        "observer": "Ian McDonald",
        "observation_date": "2025-05-10",
        "checklist": "S236438853",
        "observation_start_time": "17:57",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 16
      },
      {
        "observer": "Janelle McDonald",
        "observation_date": "2025-05-10",
        "checklist": "S235942902",
        "observation_start_time": "17:57",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 16
      },
      {
        "observer": "Madeline Wainscott",
        "observation_date": "2025-05-08",
        "checklist": "S234798414",
        "observation_start_time": "18:14",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 50
      },
      {
        "observer": "Cathy Rodrigues",
        "observation_date": "2025-05-07",
        "checklist": "S240025030",
        "observation_start_time": "13:02",
        "recent_location": "104 Channing Ln, Chapel Hill US-NC 35.89289, -79.06202, Orange",
        "num_spp": 15
      },
      {
        "observer": "Madeline Wainscott",
        "observation_date": "2025-05-03",
        "checklist": "S232728622",
        "observation_start_time": "17:24",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 39
      },
      {
        "observer": "Alex Nickley",
        "observation_date": "2025-05-03",
        "checklist": "S232664503",
        "observation_start_time": "16:34",
        "recent_location": "1001–1099 Bayberry Dr, Chapel Hill US-NC 35.89049, -79.03059, Orange",
        "num_spp": 1
      },
      {
        "observer": "Alex Nickley",
        "observation_date": "2025-05-03",
        "checklist": "S232660578",
        "observation_start_time": "16:19",
        "recent_location": "Parker Preserve, Orange",
        "num_spp": 5
      },
      {
        "observer": "Alex Nickley",
        "observation_date": "2025-05-03",
        "checklist": "S232654649",
        "observation_start_time": "16:08",
        "recent_location": "27517, Chapel Hill US-NC 35.87743, -79.02673, Orange",
        "num_spp": 4
      },
      {
        "observer": "Alex Nickley",
        "observation_date": "2025-05-03",
        "checklist": "S232642794",
        "observation_start_time": "15:39",
        "recent_location": "Sparrow Cemetery, Orange",
        "num_spp": 4
      },
      {
        "observer": "Alex Nickley",
        "observation_date": "2025-05-03",
        "checklist": "S232629018",
        "observation_start_time": "15:07",
        "recent_location": "Few Lake, Durham",
        "num_spp": 7
      },
      {
        "observer": "Alex Nickley",
        "observation_date": "2025-05-03",
        "checklist": "S232522841",
        "observation_start_time": "11:46",
        "recent_location": "5145 Barbee Chapel Rd, Durham US-NC (35.8970,-79.0053), Durham",
        "num_spp": 3
      },
      {
        "observer": "Alex Nickley",
        "observation_date": "2025-05-03",
        "checklist": "S232518261",
        "observation_start_time": "11:25",
        "recent_location": "3208 Environ Way, Chapel Hill US-NC 35.90627, -79.02204, Orange",
        "num_spp": 4
      },
      {
        "observer": "Alex Nickley",
        "observation_date": "2025-05-03",
        "checklist": "S232575920",
        "observation_start_time": "06:19",
        "recent_location": "Laurel Hill--CHBC Count Area 21, Orange",
        "num_spp": 69
      },
      {
        "observer": "Cathy Rodrigues",
        "observation_date": "2025-05-02",
        "checklist": "S233808634",
        "observation_start_time": "14:35",
        "recent_location": "104 Channing Ln, Chapel Hill US-NC 35.89290, -79.06203, Orange",
        "num_spp": 11
      },
      {
        "observer": "Cathy Rodrigues",
        "observation_date": "2025-04-30",
        "checklist": "S231107523",
        "observation_start_time": "06:51",
        "recent_location": "104 Channing Ln, Chapel Hill US-NC 35.89291, -79.06203, Orange",
        "num_spp": 10
      },
      {
        "observer": "Cathy Rodrigues",
        "observation_date": "2025-04-29",
        "checklist": "S230998349",
        "observation_start_time": "18:35",
        "recent_location": "104 Channing Ln, Chapel Hill US-NC 35.89290, -79.06204, Orange",
        "num_spp": 11
      },
      {
        "observer": "Loren Hintz",
        "observation_date": "2025-04-28",
        "checklist": "S230614664",
        "observation_start_time": "17:54",
        "recent_location": "Kings Mill, Orange",
        "num_spp": 6
      },
      {
        "observer": "Ezra H",
        "observation_date": "2025-04-27",
        "checklist": "S230057956",
        "observation_start_time": "07:29",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 38
      },
      {
        "observer": "Mel Green",
        "observation_date": "2025-04-27",
        "checklist": "S230035253",
        "observation_start_time": "07:29",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 39
      },
      {
        "observer": "Cathy Rodrigues",
        "observation_date": "2025-04-25",
        "checklist": "S229270487",
        "observation_start_time": "13:07",
        "recent_location": "104 Channing Ln, Chapel Hill US-NC 35.89289, -79.06202, Orange",
        "num_spp": 10
      },
      {
        "observer": "Cathy Rodrigues",
        "observation_date": "2025-04-24",
        "checklist": "S228934353",
        "observation_start_time": "13:37",
        "recent_location": "Chapel Hill, North Carolina, US (35.893, -79.017), Orange",
        "num_spp": 18
      },
      {
        "observer": "Roger Shaw",
        "observation_date": "2025-04-23",
        "checklist": "S228460728",
        "observation_start_time": "06:44",
        "recent_location": "Parker Preserve, Orange",
        "num_spp": 41
      },
      {
        "observer": "Cathy Rodrigues",
        "observation_date": "2025-04-22",
        "checklist": "S228130387",
        "observation_start_time": "08:20",
        "recent_location": "104 Channing Lane Home (35.893, -79.062), Orange",
        "num_spp": 7
      },
      {
        "observer": "Cathy Rodrigues",
        "observation_date": "2025-04-19",
        "checklist": "S227032230",
        "observation_start_time": "11:14",
        "recent_location": "104 Channing Lane Home (35.893, -79.062), Orange",
        "num_spp": 20
      },
      {
        "observer": "Cathy Rodrigues",
        "observation_date": "2025-04-12",
        "checklist": "S224966398",
        "observation_start_time": "13:41",
        "recent_location": "104 Channing Ln, Chapel Hill US-NC 35.89288, -79.06204, Orange",
        "num_spp": 12
      },
      {
        "observer": "Loren Hintz",
        "observation_date": "2025-04-07",
        "checklist": "S223712712",
        "observation_start_time": "11:34",
        "recent_location": "Kings Mill, Orange",
        "num_spp": 10
      },
      {
        "observer": "Jeremy Wrenn",
        "observation_date": "2025-04-06",
        "checklist": "S223645570",
        "observation_start_time": "14:33",
        "recent_location": "Walk from Planetarium, Chapel Hill, North Carolina, US (35.913, -79.052), Orange",
        "num_spp": 1
      },
      {
        "observer": "Ron Martin",
        "observation_date": "2025-04-04",
        "checklist": "S222864854",
        "observation_start_time": "08:43",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 37
      },
      {
        "observer": "Jin Bai",
        "observation_date": "2025-04-03",
        "checklist": "S222741597",
        "observation_start_time": "17:31",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 19
      },
      {
        "observer": "Fleeta Chauvigne",
        "observation_date": "2025-04-03",
        "checklist": "S222739321",
        "observation_start_time": "17:23",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 20
      },
      {
        "observer": "Jeffrey Blalock",
        "observation_date": "2025-04-03",
        "checklist": "S222655336",
        "observation_start_time": "10:20",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 11
      },
      {
        "observer": "Loren Hintz",
        "observation_date": "2025-03-31",
        "checklist": "S222189074",
        "observation_start_time": "16:33",
        "recent_location": "Kings Mill, Orange",
        "num_spp": 16
      },
      {
        "observer": "Fleeta Chauvigne",
        "observation_date": "2025-03-26",
        "checklist": "S220926486",
        "observation_start_time": "09:48",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 34
      },
      {
        "observer": "Suzanne Roberts",
        "observation_date": "2025-03-21",
        "checklist": "S219806360",
        "observation_start_time": "12:33",
        "recent_location": "North Carolina Botanical Garden, Orange",
        "num_spp": 21
      },
      {
        "observer": "Antero Topp",
        "observation_date": "2025-03-21",
        "checklist": "S219818856",
        "observation_start_time": "12:33",
        "recent_location": "North Carolina Botanical Garden, Orange",
        "num_spp": 21
      },
      {
        "observer": "Loren Hintz",
        "observation_date": "2025-03-20",
        "checklist": "S219640517",
        "observation_start_time": "13:55",
        "recent_location": "Kings Mill, Orange",
        "num_spp": 0
      },
      {
        "observer": "Loren Hintz",
        "observation_date": "2025-03-20",
        "checklist": "S219640987",
        "observation_start_time": "13:41",
        "recent_location": "Kings Mill, Orange",
        "num_spp": 15
      },
      {
        "observer": "Ellen Colodney",
        "observation_date": "2025-03-18",
        "checklist": "S219255933",
        "observation_start_time": "13:27",
        "recent_location": "North Carolina Botanical Garden, Orange",
        "num_spp": 12
      },
      {
        "observer": "Ash Ranson",
        "observation_date": "2025-03-18",
        "checklist": "S219231866",
        "observation_start_time": "11:22",
        "recent_location": "N.C. Basnight Cancer Hospital, Chapel Hill US-NC 35.90377, -79.04969, Orange",
        "num_spp": 3
      },
      {
        "observer": "Fleeta Chauvigne",
        "observation_date": "2025-03-18",
        "checklist": "S219219873",
        "observation_start_time": "08:52",
        "recent_location": "North Carolina Botanical Garden, Orange",
        "num_spp": 14
      },
      {
        "observer": "Nan Dewire",
        "observation_date": "2025-03-18",
        "checklist": "S219223208",
        "observation_start_time": "08:30",
        "recent_location": "North Carolina Botanical Garden, Orange",
        "num_spp": 17
      },
      {
        "observer": "Loren Hintz",
        "observation_date": "2025-03-17",
        "checklist": "S219122505",
        "observation_start_time": "16:50",
        "recent_location": "NC garden Elephant rock trail, Orange",
        "num_spp": 12
      },
      {
        "observer": "Nan Dewire",
        "observation_date": "2025-03-16",
        "checklist": "S218851081",
        "observation_start_time": "08:50",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 16
      },
      {
        "observer": "Nan Dewire",
        "observation_date": "2025-03-16",
        "checklist": "S218827658",
        "observation_start_time": "08:41",
        "recent_location": "Wetlands before the ford, Orange",
        "num_spp": 12
      },
      {
        "observer": "Jin Bai",
        "observation_date": "2025-03-15",
        "checklist": "S218627903",
        "observation_start_time": "08:07",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 41
      },
      {
        "observer": "Allen Hurlbert",
        "observation_date": "2025-03-14",
        "checklist": "S218432153",
        "observation_start_time": "11:17",
        "recent_location": "Wilson-Coker courtyard, Orange",
        "num_spp": 7
      },
      {
        "observer": "Nan Dewire",
        "observation_date": "2025-03-13",
        "checklist": "S218294557",
        "observation_start_time": "09:02",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 23
      },
      {
        "observer": "Allen Hurlbert",
        "observation_date": "2025-03-11",
        "checklist": "S217883433",
        "observation_start_time": "11:19",
        "recent_location": "Wilson-Coker courtyard, Orange",
        "num_spp": 8
      },
      {
        "observer": "Allen Hurlbert",
        "observation_date": "2025-03-08",
        "checklist": "S217284311",
        "observation_start_time": "13:43",
        "recent_location": "The Cedars, Durham",
        "num_spp": 9
      },
      {
        "observer": "Zane Fish",
        "observation_date": "2025-03-08",
        "checklist": "S217614668",
        "observation_start_time": "12:48",
        "recent_location": "North Carolina Botanical Garden, Orange",
        "num_spp": 23
      },
      {
        "observer": "Ash Ranson",
        "observation_date": "2025-03-08",
        "checklist": "S217318822",
        "observation_start_time": "12:48",
        "recent_location": "North Carolina Botanical Garden, Orange",
        "num_spp": 23
      },
      {
        "observer": "Cathy Rodrigues",
        "observation_date": "2025-03-08",
        "checklist": "S217276663",
        "observation_start_time": "12:13",
        "recent_location": "104 Channing Lane Home Feeder (35.893, -79.062), Orange",
        "num_spp": 20
      },
      {
        "observer": "Fleeta Chauvigne",
        "observation_date": "2025-03-07",
        "checklist": "S217043654",
        "observation_start_time": "09:09",
        "recent_location": "Wetlands before Mason Farm ford, Orange",
        "num_spp": 34
      },
      {
        "observer": "Nan Dewire",
        "observation_date": "2025-03-07",
        "checklist": "S217115823",
        "observation_start_time": "09:09",
        "recent_location": "Wetlands before Mason Farm ford, Orange",
        "num_spp": 34
      },
      {
        "observer": "Nan Dewire",
        "observation_date": "2025-03-04",
        "checklist": "S217804834",
        "observation_start_time": "16:19",
        "recent_location": "The University of North Carolina at Chapel Hill, Chapel Hill US-NC 35.89020, -79.01535, Orange",
        "num_spp": 13
      },
      {
        "observer": "Fleeta Chauvigne",
        "observation_date": "2025-03-02",
        "checklist": "S216308716",
        "observation_start_time": "14:23",
        "recent_location": "Raleigh Rd, Chapel Hill US-NC (35.9086,-79.0264), Orange",
        "num_spp": 1
      },
      {
        "observer": "Suzanne Roberts",
        "observation_date": "2025-02-26",
        "checklist": "S215517436",
        "observation_start_time": "09:03",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 10
      },
      {
        "observer": "Cathy Rodrigues",
        "observation_date": "2025-02-25",
        "checklist": "S215403310",
        "observation_start_time": "13:07",
        "recent_location": "104 Channing Lane Home Feeder (35.893, -79.062), Orange",
        "num_spp": 16
      },
      {
        "observer": "Allen Hurlbert",
        "observation_date": "2025-02-25",
        "checklist": "S215384036",
        "observation_start_time": "11:27",
        "recent_location": "Wilson-Coker courtyard, Orange",
        "num_spp": 6
      },
      {
        "observer": "Cathy Rodrigues",
        "observation_date": "2025-02-24",
        "checklist": "S215403765",
        "observation_start_time": "16:21",
        "recent_location": "104 Channing Lane Home Feeder (35.893, -79.062), Orange",
        "num_spp": 1
      },
      {
        "observer": "Allen Hurlbert",
        "observation_date": "2025-02-23",
        "checklist": "S216115466",
        "observation_start_time": "13:29",
        "recent_location": "The Cedars, Durham",
        "num_spp": 16
      },
      {
        "observer": "Lauren Greene",
        "observation_date": "2025-02-23",
        "checklist": "S215072161",
        "observation_start_time": "13:18",
        "recent_location": "North Carolina Botanical Garden, Orange",
        "num_spp": 11
      },
      {
        "observer": "Nan Dewire",
        "observation_date": "2025-02-23",
        "checklist": "S215045897",
        "observation_start_time": "10:04",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 29
      },
      {
        "observer": "Nan Dewire",
        "observation_date": "2025-02-23",
        "checklist": "S215020436",
        "observation_start_time": "09:22",
        "recent_location": "Parker Preserve, Orange",
        "num_spp": 16
      },
      {
        "observer": "Cathy Rodrigues",
        "observation_date": "2025-02-19",
        "checklist": "S214428108",
        "observation_start_time": "12:51",
        "recent_location": "104 Channing Lane Home Feeder (35.893, -79.062), Orange",
        "num_spp": 21
      },
      {
        "observer": "Cathy Rodrigues",
        "observation_date": "2025-02-15",
        "checklist": "S213658323",
        "observation_start_time": "12:29",
        "recent_location": "555 Old Mason Farm Road, Chapel Hill, North Carolina, US (35.894, -79.017), Orange",
        "num_spp": 9
      },
      {
        "observer": "Lauren Greene",
        "observation_date": "2025-02-14",
        "checklist": "S213312598",
        "observation_start_time": "16:26",
        "recent_location": "North Carolina Botanical Garden, Orange",
        "num_spp": 6
      },
      {
        "observer": "Alison O",
        "observation_date": "2025-02-14",
        "checklist": "S213931769",
        "observation_start_time": "11:00",
        "recent_location": "North Carolina Botanical Garden, Orange",
        "num_spp": 6
      },
      {
        "observer": "Nan Dewire",
        "observation_date": "2025-02-10",
        "checklist": "S213077372",
        "observation_start_time": "12:04",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 26
      },
      {
        "observer": "Allen Hurlbert",
        "observation_date": "2025-02-06",
        "checklist": "S212187163",
        "observation_start_time": "10:11",
        "recent_location": "University of North Carolina-Chapel Hill main campus, Orange",
        "num_spp": 16
      },
      {
        "observer": "Allen Hurlbert",
        "observation_date": "2025-02-02",
        "checklist": "S211727547",
        "observation_start_time": "14:20",
        "recent_location": "The Cedars, Durham",
        "num_spp": 19
      },
      {
        "observer": "Nan Dewire",
        "observation_date": "2025-01-31",
        "checklist": "S211375075",
        "observation_start_time": "12:10",
        "recent_location": "The University of North Carolina at Chapel Hill, Chapel Hill US-NC (35.8935,-79.0174), Orange",
        "num_spp": 9
      },
      {
        "observer": "Fleeta Chauvigne",
        "observation_date": "2025-01-31",
        "checklist": "S211376566",
        "observation_start_time": "12:07",
        "recent_location": "Wetlands before Mason Farm ford, Orange",
        "num_spp": 21
      },
      {
        "observer": "Fleeta Chauvigne",
        "observation_date": "2025-01-31",
        "checklist": "S211380880",
        "observation_start_time": "09:16",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 38
      },
      {
        "observer": "Nan Dewire",
        "observation_date": "2025-01-31",
        "checklist": "S211372901",
        "observation_start_time": "09:16",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 38
      },
      {
        "observer": "Nan Dewire",
        "observation_date": "2025-01-29",
        "checklist": "S211348501",
        "observation_start_time": "15:33",
        "recent_location": "The University of North Carolina at Chapel Hill, Chapel Hill US-NC 35.88525, -79.01871, Orange",
        "num_spp": 9
      },
      {
        "observer": "Allen Hurlbert",
        "observation_date": "2025-01-28",
        "checklist": "S211046612",
        "observation_start_time": "15:36",
        "recent_location": "Wilson-Mitchell Courtyard, Orange",
        "num_spp": 3
      },
      {
        "observer": "Patsy Bailey",
        "observation_date": "2025-01-25",
        "checklist": "S210639439",
        "observation_start_time": "13:08",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 18
      },
      {
        "observer": "Patsy Bailey",
        "observation_date": "2025-01-25",
        "checklist": "S210629945",
        "observation_start_time": "12:08",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 17
      },
      {
        "observer": "Suzanne Roberts",
        "observation_date": "2025-01-19",
        "checklist": "S209917466",
        "observation_start_time": "07:54",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 27
      },
      {
        "observer": "Vicki Nebes",
        "observation_date": "2025-01-19",
        "checklist": "S209931009",
        "observation_start_time": "07:54",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 27
      },
      {
        "observer": "Emma Powers",
        "observation_date": "2025-01-19",
        "checklist": "S209948858",
        "observation_start_time": "07:54",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 27
      },
      {
        "observer": "Matt Moore",
        "observation_date": "2025-01-19",
        "checklist": "S211123512",
        "observation_start_time": "07:54",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 27
      },
      {
        "observer": "Cathy Rodrigues",
        "observation_date": "2025-01-17",
        "checklist": "S209609987",
        "observation_start_time": "11:01",
        "recent_location": "104 Channing Lane Home (35.893, -79.062), Orange",
        "num_spp": 16
      },
      {
        "observer": "Fleeta Chauvigne",
        "observation_date": "2025-01-11",
        "checklist": "S208897392",
        "observation_start_time": "14:54",
        "recent_location": "Wetlands before Mason Farm ford, Orange",
        "num_spp": 16
      },
      {
        "observer": "Fleeta Chauvigne",
        "observation_date": "2025-01-07",
        "checklist": "S208424204",
        "observation_start_time": "15:14",
        "recent_location": "1008–1030 S Hamilton Rd, Chapel Hill US-NC 35.90782, -79.02384, Orange",
        "num_spp": 1
      },
      {
        "observer": "Fleeta Chauvigne",
        "observation_date": "2025-01-04",
        "checklist": "S208002498",
        "observation_start_time": "13:49",
        "recent_location": "1008–1030 S Hamilton Rd, Chapel Hill US-NC 35.90782, -79.02384, Orange",
        "num_spp": 1
      },
      {
        "observer": "Cathy Rodrigues",
        "observation_date": "2025-01-02",
        "checklist": "S207663856",
        "observation_start_time": "11:07",
        "recent_location": "104 Channing Lane Home (35.893, -79.062), Orange",
        "num_spp": 17
      },
      {
        "observer": "Vicki Nebes",
        "observation_date": "2025-01-01",
        "checklist": "S207479971",
        "observation_start_time": "09:20",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 26
      },
      {
        "observer": "Cathy Rodrigues",
        "observation_date": "2024-12-31",
        "checklist": "S207328071",
        "observation_start_time": "10:44",
        "recent_location": "104 Channing Lane Home (35.893, -79.062), Orange",
        "num_spp": 18
      },
      {
        "observer": "Cathy Rodrigues",
        "observation_date": "2024-12-25",
        "checklist": "S206542520",
        "observation_start_time": "14:12",
        "recent_location": "104 Channing Lane Home (35.893, -79.062), Orange",
        "num_spp": 17
      },
      {
        "observer": "Alan Avakian",
        "observation_date": "2024-12-19",
        "checklist": "S205940858",
        "observation_start_time": "14:46",
        "recent_location": "401 Rhododendron Drive, Chapel Hill, North Carolina, US (35.882, -79.035), Orange",
        "num_spp": 19
      },
      {
        "observer": "Fleeta Chauvigne",
        "observation_date": "2024-12-19",
        "checklist": "S205924364",
        "observation_start_time": "14:07",
        "recent_location": "North Carolina Botanical Garden, Orange",
        "num_spp": 5
      },
      {
        "observer": "Cathy Rodrigues",
        "observation_date": "2024-12-17",
        "checklist": "S205760586",
        "observation_start_time": "14:42",
        "recent_location": "104 Channing Lane Home (35.893, -79.062), Orange",
        "num_spp": 16
      },
      {
        "observer": "Cathy Rodrigues",
        "observation_date": "2024-12-15",
        "checklist": "S205506185",
        "observation_start_time": "12:19",
        "recent_location": "104 Channing Lane Home (35.893, -79.062), Orange",
        "num_spp": 21
      },
      {
        "observer": "Suzanne Roberts",
        "observation_date": "2024-12-15",
        "checklist": "S205476817",
        "observation_start_time": "09:15",
        "recent_location": "Piedmont Nature Trail, Orange",
        "num_spp": 21
      },
      {
        "observer": "Antero Topp",
        "observation_date": "2024-12-15",
        "checklist": "S205516453",
        "observation_start_time": "09:15",
        "recent_location": "Piedmont Nature Trail, Orange",
        "num_spp": 21
      },
      {
        "observer": "Cathy Rodrigues",
        "observation_date": "2024-12-14",
        "checklist": "S205347414",
        "observation_start_time": "10:15",
        "recent_location": "104 Channing Lane Home (35.893, -79.062), Orange",
        "num_spp": 1
      },
      {
        "observer": "Jeremy Wrenn",
        "observation_date": "2024-12-08",
        "checklist": "S204872754",
        "observation_start_time": "17:10",
        "recent_location": "105 East Cameron Avenue, Chapel Hill, North Carolina, US (35.912, -79.053), Orange",
        "num_spp": 4
      },
      {
        "observer": "Jeremy Wrenn",
        "observation_date": "2024-12-08",
        "checklist": "S204872795",
        "observation_start_time": "15:37",
        "recent_location": "105 East Cameron Avenue, Chapel Hill, North Carolina, US (35.912, -79.053), Orange",
        "num_spp": 1
      },
      {
        "observer": "Jin Bai",
        "observation_date": "2024-12-07",
        "checklist": "S204706583",
        "observation_start_time": "12:08",
        "recent_location": "Baity Hill at Mason Farm, Orange",
        "num_spp": 1
      },
      {
        "observer": "Cathy Rodrigues",
        "observation_date": "2024-12-03",
        "checklist": "S204380777",
        "observation_start_time": "11:28",
        "recent_location": "104 Channing Lane Home (35.893, -79.062), Orange",
        "num_spp": 15
      },
      {
        "observer": "Mark Rodrigues",
        "observation_date": "2024-12-01",
        "checklist": "S204231197",
        "observation_start_time": "12:05",
        "recent_location": "104 Channing Lane Home (35.893, -79.062), Orange",
        "num_spp": 17
      },
      {
        "observer": "Cathy Rodrigues",
        "observation_date": "2024-12-01",
        "checklist": "S204202988",
        "observation_start_time": "12:05",
        "recent_location": "104 Channing Lane Home (35.893, -79.062), Orange",
        "num_spp": 17
      },
      {
        "observer": "Cathy Rodrigues",
        "observation_date": "2024-11-30",
        "checklist": "S204074844",
        "observation_start_time": "11:38",
        "recent_location": "104 Channing Lane Home (35.893, -79.062), Orange",
        "num_spp": 12
      },
      {
        "observer": "Cathy Rodrigues",
        "observation_date": "2024-11-29",
        "checklist": "S203979969",
        "observation_start_time": "13:25",
        "recent_location": "104 Channing Lane Home (35.893, -79.062), Orange",
        "num_spp": 15
      },
      {
        "observer": "Alan Avakian",
        "observation_date": "2024-11-27",
        "checklist": "S203776769",
        "observation_start_time": "08:12",
        "recent_location": "720 Finley Golf Course Road, Chapel Hill, North Carolina, US (35.892, -79.016), Orange",
        "num_spp": 38
      },
      {
        "observer": "Fleeta Chauvigne",
        "observation_date": "2024-11-23",
        "checklist": "S203367320",
        "observation_start_time": "12:22",
        "recent_location": "Wetlands before Mason Farm ford, Orange",
        "num_spp": 8
      },
      {
        "observer": "Fleeta Chauvigne",
        "observation_date": "2024-11-23",
        "checklist": "S203365788",
        "observation_start_time": "11:22",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 19
      },
      {
        "observer": "Mel Green",
        "observation_date": "2024-11-23",
        "checklist": "S203414421",
        "observation_start_time": "11:22",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 19
      },
      {
        "observer": "Fleeta Chauvigne",
        "observation_date": "2024-11-19",
        "checklist": "S203013841",
        "observation_start_time": "09:21",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 34
      },
      {
        "observer": "Fleeta Chauvigne",
        "observation_date": "2024-11-15",
        "checklist": "S202563314",
        "observation_start_time": "11:53",
        "recent_location": "Wetlands before Mason Farm ford, Orange",
        "num_spp": 18
      },
      {
        "observer": "Fleeta Chauvigne",
        "observation_date": "2024-11-15",
        "checklist": "S202560782",
        "observation_start_time": "10:27",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 14
      },
      {
        "observer": "Cathy Rodrigues",
        "observation_date": "2024-11-13",
        "checklist": "S202397912",
        "observation_start_time": "15:59",
        "recent_location": "104 Channing Lane Home (35.893, -79.062), Orange",
        "num_spp": 12
      },
      {
        "observer": "Nan Dewire",
        "observation_date": "2024-11-03",
        "checklist": "S201315196",
        "observation_start_time": "15:14",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 18
      },
      {
        "observer": "Cathy Rodrigues",
        "observation_date": "2024-11-03",
        "checklist": "S201292337",
        "observation_start_time": "13:20",
        "recent_location": "104 Channing Lane Home (35.893, -79.062), Orange",
        "num_spp": 13
      },
      {
        "observer": "Nan Dewire",
        "observation_date": "2024-10-27",
        "checklist": "S200628102",
        "observation_start_time": "10:24",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 26
      },
      {
        "observer": "Cathy Rodrigues",
        "observation_date": "2024-10-25",
        "checklist": "S200226456",
        "observation_start_time": "15:23",
        "recent_location": "104 Channing Lane Home (35.893, -79.062), Orange",
        "num_spp": 10
      },
      {
        "observer": "Nan Dewire",
        "observation_date": "2024-10-25",
        "checklist": "S200226059",
        "observation_start_time": "14:28",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 23
      },
      {
        "observer": "Mark Rodrigues",
        "observation_date": "2024-10-17",
        "checklist": "S199259534",
        "observation_start_time": "11:17",
        "recent_location": "104 Channing Lane Home (35.893, -79.062), Orange",
        "num_spp": 13
      },
      {
        "observer": "Cathy Rodrigues",
        "observation_date": "2024-10-17",
        "checklist": "S199229729",
        "observation_start_time": "11:17",
        "recent_location": "104 Channing Lane Home (35.893, -79.062), Orange",
        "num_spp": 13
      },
      {
        "observer": "Tim Lamb",
        "observation_date": "2024-10-16",
        "checklist": "S199151881",
        "observation_start_time": "13:49",
        "recent_location": "North Carolina Botanical Garden, Orange",
        "num_spp": 17
      },
      {
        "observer": "Lucretia Kinney",
        "observation_date": "2024-10-14",
        "checklist": "S198944400",
        "observation_start_time": "09:55",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 23
      },
      {
        "observer": "Nan Dewire",
        "observation_date": "2024-10-11",
        "checklist": "S198855001",
        "observation_start_time": "09:15",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 26
      },
      {
        "observer": "Nan Dewire",
        "observation_date": "2024-10-09",
        "checklist": "S198109083",
        "observation_start_time": "09:04",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 18
      },
      {
        "observer": "Nan Dewire",
        "observation_date": "2024-10-09",
        "checklist": "S198101454",
        "observation_start_time": "08:37",
        "recent_location": "Wetlands before the ford, Orange",
        "num_spp": 19
      },
      {
        "observer": "Stephen Matadobra",
        "observation_date": "2024-10-05",
        "checklist": "S197620878",
        "observation_start_time": "07:49",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 33
      },
      {
        "observer": "Fleeta Chauvigne",
        "observation_date": "2024-10-02",
        "checklist": "S197355212",
        "observation_start_time": "18:39",
        "recent_location": "Davie Poplar, UNC campus, Orange",
        "num_spp": 7
      },
      {
        "observer": "Brooks Emanuel",
        "observation_date": "2024-10-02",
        "checklist": "S197308812",
        "observation_start_time": "18:39",
        "recent_location": "Davie Poplar, UNC campus, Orange",
        "num_spp": 7
      },
      {
        "observer": "Nan Dewire",
        "observation_date": "2024-10-02",
        "checklist": "S197298126",
        "observation_start_time": "18:39",
        "recent_location": "Davie Poplar, UNC campus, Orange",
        "num_spp": 7
      },
      {
        "observer": "Catherine Berman",
        "observation_date": "2024-10-02",
        "checklist": "S197843694",
        "observation_start_time": "18:39",
        "recent_location": "Davie Poplar, UNC campus, Orange",
        "num_spp": 7
      },
      {
        "observer": "Matt Spangler",
        "observation_date": "2024-09-22",
        "checklist": "S196170896",
        "observation_start_time": "19:06",
        "recent_location": "Davie Poplar, Chapel Hill US-NC (35.9130,-79.0516), Orange",
        "num_spp": 3
      },
      {
        "observer": "Wayne Covington",
        "observation_date": "2024-09-21",
        "checklist": "S195939512",
        "observation_start_time": "11:42",
        "recent_location": "UNC Chapel Hill--Coker Arboretum, Orange",
        "num_spp": 2
      },
      {
        "observer": "Jin Bai",
        "observation_date": "2024-09-21",
        "checklist": "S195909473",
        "observation_start_time": "09:15",
        "recent_location": "The University of North Carolina at Chapel Hill, Chapel Hill US-NC 35.90696, -79.04625, Orange",
        "num_spp": 1
      },
      {
        "observer": "Jin Bai",
        "observation_date": "2024-09-21",
        "checklist": "S195909337",
        "observation_start_time": "09:14",
        "recent_location": "The University of North Carolina at Chapel Hill, Chapel Hill US-NC 35.90710, -79.04627, Orange",
        "num_spp": 1
      },
      {
        "observer": "Nan Dewire",
        "observation_date": "2024-09-19",
        "checklist": "S195675219",
        "observation_start_time": "09:09",
        "recent_location": "Service road, Orange",
        "num_spp": 17
      },
      {
        "observer": "Nan Dewire",
        "observation_date": "2024-09-19",
        "checklist": "S195670223",
        "observation_start_time": "08:58",
        "recent_location": "Wetlands before the ford, Orange",
        "num_spp": 8
      },
      {
        "observer": "Jin Bai",
        "observation_date": "2024-09-18",
        "checklist": "S195626262",
        "observation_start_time": "19:00",
        "recent_location": "The University of North Carolina at Chapel Hill, Chapel Hill US-NC (35.9130,-79.0519), Orange",
        "num_spp": 4
      },
      {
        "observer": "Nan Dewire",
        "observation_date": "2024-09-18",
        "checklist": "S195850699",
        "observation_start_time": "18:51",
        "recent_location": "Davie Poplar, UNC campus, Orange",
        "num_spp": 3
      },
      {
        "observer": "Brooke Mahany",
        "observation_date": "2024-09-18",
        "checklist": "S195612946",
        "observation_start_time": "17:17",
        "recent_location": "Old Chapel Hill Cemetery (UNC-CH, Chapel Hill), Orange",
        "num_spp": 1
      },
      {
        "observer": "Brooke Mahany",
        "observation_date": "2024-09-18",
        "checklist": "S210210679",
        "observation_start_time": "17:17",
        "recent_location": "Old Chapel Hill Cemetery (UNC-CH, Chapel Hill), Orange",
        "num_spp": 1
      },
      {
        "observer": "Jin Bai",
        "observation_date": "2024-09-15",
        "checklist": "S195203041",
        "observation_start_time": "08:07",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 18
      },
      {
        "observer": "C.C. King",
        "observation_date": "2024-09-14",
        "checklist": "S195068380",
        "observation_start_time": "08:47",
        "recent_location": "The University of North Carolina at Chapel Hill, Chapel Hill US-NC 35.89136, -79.01636, Orange",
        "num_spp": 16
      },
      {
        "observer": "Jin Bai",
        "observation_date": "2024-09-12",
        "checklist": "S194842059",
        "observation_start_time": "10:46",
        "recent_location": "Baity Hill at Mason Farm, Orange",
        "num_spp": 1
      },
      {
        "observer": "Nan Dewire",
        "observation_date": "2024-09-12",
        "checklist": "S194850696",
        "observation_start_time": "10:24",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 25
      },
      {
        "observer": "Nan Dewire",
        "observation_date": "2024-09-12",
        "checklist": "S194838890",
        "observation_start_time": "10:08",
        "recent_location": "Wetlands before the ford, Orange",
        "num_spp": 9
      },
      {
        "observer": "Jin Bai",
        "observation_date": "2024-09-10",
        "checklist": "S194630630",
        "observation_start_time": "09:35",
        "recent_location": "Baity Hill at Mason Farm, Orange",
        "num_spp": 1
      },
      {
        "observer": "Nan Dewire",
        "observation_date": "2024-09-08",
        "checklist": "S194694879",
        "observation_start_time": "16:24",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 11
      },
      {
        "observer": "Curtis Brooks",
        "observation_date": "2024-09-08",
        "checklist": "S195091141",
        "observation_start_time": "16:20",
        "recent_location": "Wetlands before the ford, Orange",
        "num_spp": 4
      },
      {
        "observer": "Nan Dewire",
        "observation_date": "2024-09-08",
        "checklist": "S194460271",
        "observation_start_time": "16:20",
        "recent_location": "Wetlands before the ford, Orange",
        "num_spp": 4
      },
      {
        "observer": "Cathy Rodrigues",
        "observation_date": "2024-09-06",
        "checklist": "S194174198",
        "observation_start_time": "14:34",
        "recent_location": "104 Channing Lane Home (35.893, -79.062), Orange",
        "num_spp": 12
      },
      {
        "observer": "Susan Campbell",
        "observation_date": "2024-08-31",
        "checklist": "S193419123",
        "observation_start_time": "12:29",
        "recent_location": "North Carolina Botanical Garden, Orange",
        "num_spp": 11
      },
      {
        "observer": "Mark Rodrigues",
        "observation_date": "2024-08-29",
        "checklist": "S197629533",
        "observation_start_time": "12:13",
        "recent_location": "104 Channing Lane Home (35.893, -79.062), Orange",
        "num_spp": 9
      },
      {
        "observer": "Cathy Rodrigues",
        "observation_date": "2024-08-29",
        "checklist": "S193173889",
        "observation_start_time": "12:13",
        "recent_location": "104 Channing Lane Home (35.893, -79.062), Orange",
        "num_spp": 9
      },
      {
        "observer": "Jin Bai",
        "observation_date": "2024-08-27",
        "checklist": "S192919127",
        "observation_start_time": "00:26",
        "recent_location": "Baity Hill at Mason Farm, Orange",
        "num_spp": 1
      },
      {
        "observer": "Jin Bai",
        "observation_date": "2024-08-24",
        "checklist": "S192548613",
        "observation_start_time": "07:33",
        "recent_location": "The University of North Carolina at Chapel Hill, Chapel Hill US-NC 35.89832, -79.04218, Orange",
        "num_spp": 1
      },
      {
        "observer": "Jin Bai",
        "observation_date": "2024-08-24",
        "checklist": "S192537928",
        "observation_start_time": "04:32",
        "recent_location": "Baity Hill at Mason Farm, Orange",
        "num_spp": 1
      },
      {
        "observer": "Jin Bai",
        "observation_date": "2024-08-21",
        "checklist": "S192273828",
        "observation_start_time": "13:49",
        "recent_location": "Baity Hill at Mason Farm, Orange",
        "num_spp": 1
      },
      {
        "observer": "Jin Bai",
        "observation_date": "2024-08-21",
        "checklist": "S192217308",
        "observation_start_time": "00:27",
        "recent_location": "Baity Hill at Mason Farm, Orange",
        "num_spp": 1
      },
      {
        "observer": "Jin Bai",
        "observation_date": "2024-08-17",
        "checklist": "S191752652",
        "observation_start_time": "07:59",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 31
      },
      {
        "observer": "Jin Bai",
        "observation_date": "2024-08-12",
        "checklist": "S191200143",
        "observation_start_time": "12:59",
        "recent_location": "Baity Hill at Mason Farm, Orange",
        "num_spp": 1
      },
      {
        "observer": "Nan Dewire",
        "observation_date": "2024-08-09",
        "checklist": "S190871658",
        "observation_start_time": "12:11",
        "recent_location": "Meadowmont Village, Chapel Hill US-NC (35.9065,-79.0102), Orange",
        "num_spp": 1
      },
      {
        "observer": "Jin Bai",
        "observation_date": "2024-08-09",
        "checklist": "S190774002",
        "observation_start_time": "11:45",
        "recent_location": "Baity Hill at Mason Farm, Orange",
        "num_spp": 1
      },
      {
        "observer": "Jin Bai",
        "observation_date": "2024-08-08",
        "checklist": "S190688868",
        "observation_start_time": "14:46",
        "recent_location": "Baity Hill at Mason Farm, Orange",
        "num_spp": 1
      },
      {
        "observer": "Jin Bai",
        "observation_date": "2024-08-07",
        "checklist": "S190608130",
        "observation_start_time": "18:59",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 23
      },
      {
        "observer": "Nan Dewire",
        "observation_date": "2024-08-06",
        "checklist": "S190442445",
        "observation_start_time": "11:00",
        "recent_location": "Wetlands before the ford, Orange",
        "num_spp": 1
      },
      {
        "observer": "Jin Bai",
        "observation_date": "2024-08-06",
        "checklist": "S190437094",
        "observation_start_time": "10:18",
        "recent_location": "Baity Hill at Mason Farm, Orange",
        "num_spp": 1
      },
      {
        "observer": "Suzanne Roberts",
        "observation_date": "2024-08-04",
        "checklist": "S196477030",
        "observation_start_time": "19:58",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 5
      },
      {
        "observer": "Curtis Brooks",
        "observation_date": "2024-08-03",
        "checklist": "S190059162",
        "observation_start_time": "10:51",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 16
      },
      {
        "observer": "Nan Dewire",
        "observation_date": "2024-08-03",
        "checklist": "S190050804",
        "observation_start_time": "10:51",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 16
      },
      {
        "observer": "Curtis Brooks",
        "observation_date": "2024-08-03",
        "checklist": "S190059167",
        "observation_start_time": "10:41",
        "recent_location": "Wetlands before the ford, Orange",
        "num_spp": 8
      },
      {
        "observer": "Nan Dewire",
        "observation_date": "2024-08-03",
        "checklist": "S190040829",
        "observation_start_time": "10:41",
        "recent_location": "Wetlands before the ford, Orange",
        "num_spp": 8
      },
      {
        "observer": "Nan Dewire",
        "observation_date": "2024-08-03",
        "checklist": "S190035820",
        "observation_start_time": "10:18",
        "recent_location": "The University of North Carolina at Chapel Hill, Chapel Hill US-NC 35.88981, -79.00883, Durham",
        "num_spp": 2
      },
      {
        "observer": "Nan Dewire",
        "observation_date": "2024-08-03",
        "checklist": "S190033351",
        "observation_start_time": "09:23",
        "recent_location": "The University of North Carolina at Chapel Hill, Chapel Hill US-NC 35.89306, -79.01589, Orange",
        "num_spp": 17
      },
      {
        "observer": "Jeffrey Blalock",
        "observation_date": "2024-08-02",
        "checklist": "S189922201",
        "observation_start_time": "11:50",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 7
      },
      {
        "observer": "Jeffrey Blalock",
        "observation_date": "2024-08-02",
        "checklist": "S189918943",
        "observation_start_time": "10:35",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 16
      },
      {
        "observer": "David Schroder",
        "observation_date": "2024-08-02",
        "checklist": "S189908751",
        "observation_start_time": "10:18",
        "recent_location": "The University of North Carolina at Chapel Hill, Chapel Hill US-NC 35.89058, -79.01108, Durham",
        "num_spp": 8
      },
      {
        "observer": "Jeffrey Blalock",
        "observation_date": "2024-08-02",
        "checklist": "S189909094",
        "observation_start_time": "10:10",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 6
      },
      {
        "observer": "David Schroder",
        "observation_date": "2024-08-02",
        "checklist": "S189906894",
        "observation_start_time": "10:06",
        "recent_location": "The University of North Carolina at Chapel Hill, Chapel Hill US-NC 35.89369, -79.01709, Orange",
        "num_spp": 6
      },
      {
        "observer": "Zane Fish",
        "observation_date": "2024-08-01",
        "checklist": "S189850540",
        "observation_start_time": "19:56",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 26
      },
      {
        "observer": "Ash Ranson",
        "observation_date": "2024-08-01",
        "checklist": "S189893249",
        "observation_start_time": "19:56",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 26
      },
      {
        "observer": "Richard Snow",
        "observation_date": "2024-08-01",
        "checklist": "S189908240",
        "observation_start_time": "18:26",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 20
      },
      {
        "observer": "Zane Fish",
        "observation_date": "2024-07-31",
        "checklist": "S189744317",
        "observation_start_time": "19:13",
        "recent_location": "Mason Farm Pond, Orange",
        "num_spp": 22
      },
      {
        "observer": "Ash Ranson",
        "observation_date": "2024-07-31",
        "checklist": "S189893251",
        "observation_start_time": "19:13",
        "recent_location": "Mason Farm Pond, Orange",
        "num_spp": 22
      },
      {
        "observer": "Nan Dewire",
        "observation_date": "2024-07-31",
        "checklist": "S189679554",
        "observation_start_time": "11:06",
        "recent_location": "Wetlands before the ford, Orange",
        "num_spp": 1
      },
      {
        "observer": "Nan Dewire",
        "observation_date": "2024-07-31",
        "checklist": "S189678986",
        "observation_start_time": "09:30",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 18
      },
      {
        "observer": "Nan Dewire",
        "observation_date": "2024-07-30",
        "checklist": "S189536110",
        "observation_start_time": "09:31",
        "recent_location": "Wetlands before the ford, Orange",
        "num_spp": 18
      },
      {
        "observer": "Jin Bai",
        "observation_date": "2024-07-29",
        "checklist": "S189433319",
        "observation_start_time": "13:18",
        "recent_location": "Baity Hill at Mason Farm, Orange",
        "num_spp": 1
      },
      {
        "observer": "Nan Dewire",
        "observation_date": "2024-07-28",
        "checklist": "S189337089",
        "observation_start_time": "14:32",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 14
      },
      {
        "observer": "Curtis Brooks",
        "observation_date": "2024-07-28",
        "checklist": "S189315638",
        "observation_start_time": "14:27",
        "recent_location": "Wetlands before the ford, Orange",
        "num_spp": 3
      },
      {
        "observer": "Nan Dewire",
        "observation_date": "2024-07-28",
        "checklist": "S189301598",
        "observation_start_time": "14:27",
        "recent_location": "Wetlands before the ford, Orange",
        "num_spp": 3
      },
      {
        "observer": "Linda Robinson",
        "observation_date": "2024-07-27",
        "checklist": "S189103263",
        "observation_start_time": "11:09",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 11
      },
      {
        "observer": "Richard Snow",
        "observation_date": "2024-07-27",
        "checklist": "S189098256",
        "observation_start_time": "11:09",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 11
      },
      {
        "observer": "Nan Dewire",
        "observation_date": "2024-07-27",
        "checklist": "S189071122",
        "observation_start_time": "09:24",
        "recent_location": "Mason Farm Biological Reserve, Orange",
        "num_spp": 23
      },
      {
        "observer": "Nan Dewire",
        "observation_date": "2024-07-27",
        "checklist": "S189052037",
        "observation_start_time": "09:12",
        "recent_location": "Wetlands before the ford, Orange",
        "num_spp": 17
      },
      {
        "observer": "Nan Dewire",
        "observation_date": "2024-07-26",
        "checklist": "S188923378",
        "observation_start_time": "10:38",
        "recent_location": "The University of North Carolina at Chapel Hill, Chapel Hill US-NC 35.89149, -79.01275, Orange",
        "num_spp": 17
      },
      {
        "observer": "Nan Dewire",
        "observation_date": "2024-07-26",
        "checklist": "S188912638",
        "observation_start_time": "09:30",
        "recent_location": "Wetlands before the ford, Orange",
        "num_spp": 31
      },
      {
        "observer": "Nan Dewire",
        "observation_date": "2024-07-25",
        "checklist": "S188697584",
        "observation_start_time": "09:51",
        "recent_location": "Wetlands before the ford, Orange",
        "num_spp": 9
      }
    ]
  },
  "MOST_RECENT_EBD_DATE": "2025-05-27",
  "NCBA_EBD_VER": "2025-05-27",
  "NCBA_STAFF_PRIORITY": "",
  "REPORT_URL": "https://drive.google.com/file/d/1-dzbqgw9_zL22iMMhvQGz7b6jp9MiT4f/view?usp=sharing",
  "s7EligibleChecklists": {
    "S224966398": {
      "SEI": "S224966398",
      "OBS_DATE": "2025-04-12",
      "LATITUDE": 35.89288,
      "LONGITUDE": -79.062043,
      "SPP_LIST": [
        "Eastern Towhee"
      ]
    },
    "S227032230": {
      "SEI": "S227032230",
      "OBS_DATE": "2025-04-19",
      "LATITUDE": 35.8929133,
      "LONGITUDE": -79.0620463,
      "SPP_LIST": [
        "Eastern Bluebird",
        "White-eyed Vireo",
        "Wood Thrush"
      ]
    },
    "S222741597": {
      "SEI": "S222741597",
      "OBS_DATE": "2025-04-03",
      "LATITUDE": 35.8849444,
      "LONGITUDE": -79.0145083,
      "SPP_LIST": [
        "Northern Cardinal",
        "Northern Parula",
        "Tufted Titmouse",
        "White-eyed Vireo"
      ]
    },
    "S230614664": {
      "SEI": "S230614664",
      "OBS_DATE": "2025-04-28",
      "LATITUDE": 35.8952328,
      "LONGITUDE": -79.0405194,
      "SPP_LIST": [
        "Wood Thrush"
      ]
    },
    "S240025030": {
      "SEI": "S240025030",
      "OBS_DATE": "2025-05-07",
      "LATITUDE": 35.89289,
      "LONGITUDE": -79.062016,
      "SPP_LIST": [
        "Pine Warbler"
      ]
    }
  }
}

pdf = PDF(bsd)
# pdf.set_title("20000 Leagues Under the Seas")
# pdf.set_author("Jules Verne")
# pdf.print_chapter(1, "A RUNAWAY REEF")
# pdf.print_chapter(2, "THE PROS AND CONS")
file_name = f'{bsd["ID_NCBA_BLOCK"]}_Report.pdf'
file_path = f'block_reports/{file_name}'
pdf.output(file_path)

# file_url = upload_file_to_drive(file_path, file_name)
# print(file_url)