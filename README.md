# Hope's Corner Waiver Submission App

A Shiny for Python web application that allows unhoused individuals to electronically sign waivers for Hope's Corner's shower and laundry program services.

## Key Features

- Bilingual support (English/Spanish)
- Electronic signature capture with HTML5 Canvas
- Complete form validation
- Screenshot capture of completed waivers
- Direct submission to SharePoint Excel spreadsheet via Microsoft Graph API
- Responsive design for both desktop and mobile devices

## Environment Setup

Create a `.env` file with the following configuration:
```
AZURE_TENANT_ID=YOUR_TENANT_ID
AZURE_CLIENT_ID=YOUR_CLIENT_ID
AZURE_CLIENT_SECRET=YOUR_CLIENT_SECRET
SHAREPOINT_SITE_URL=https://yourtenant.sharepoint.com/sites/yoursite
SHAREPOINT_EXCEL_FILE_PATH=/Shared Documents/waiver_submissions.xlsx
SHAREPOINT_WORKSHEET_NAME=Sheet1
```

## Local Development

1. Install dependencies: `pip install -r requirements.txt`
2. Run the app: `python -m shiny run --reload app.py`
3. Open the provided localhost URL in your browser

## Deployment

The app can be deployed to Posit Connect or shinyapps.io using rsconnect-python:

```bash
rsconnect deploy shiny . \
  --name <account_name> \
  --title hopes_corner_waiver
```

Note: Ensure all environment variables are properly configured in your deployment environment.
