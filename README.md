# gpc-pricer
This script is designed to be deployed as a cloud function and takes the input of a SKU description from the GCP public pricing table and returns the list price for it.
It is not setup to search for nearest neighbor, nor does it reject if the table in memory has multiple entries for the same SKU description (such as if the pricing is tiered).That logic may be built in later.
