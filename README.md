# NC Bird Atlas Data Management

The [NC Bird Atlas](https://ncbirdatlas.org) promotes the use of eBird to collect all data for the project. However, we store these data in a MongoDB implementation we call the Atlas Cache. Updating and augmenting data from eBird (via periodic projects or EBD downloads) is accomplished through the included Python Scripts.


## Upload Procedures

* `ebd_downloads_to_mongodb.ipynb`
    * Converts standard EBD formatted download to NCBA format
    * Augments select fields for use in the Atlas
    * Updates records that have changed since the last upload.
* `ebd_projects_to_mongodb.ipynb`
    * Converts "projects" file from the [eBird NCBA Project page](https://ebird.org/projects/1005/admin) to the NCBA format
    * Augments select fields for use in the Atlas
    * Updates records that have changed since the last upload