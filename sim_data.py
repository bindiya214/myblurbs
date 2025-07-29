# sim_data.py

SIM_Cases = {
    "Holiday Management": { # This remains the main "cycle"
        "Incorrect CTI": { # This now serves as both the "stage" and directly holds the blurb
            "blurb": "Hi Team,\n\nThis is an incorrect CTI.\nRaise a new TT for the correct CTI.\nResolving this case."
        },
        "Pickup Constraint (SH Deployed)": {
            "blurb": "Hi Team,\n\nDue to pickup constraint from Last mile pickup team, Ship Holiday(SH) was deployed for the seller.\nUnfortunately, We were not be able to revoke the holiday\nHence resolving"
        },
        "No Deployment Actions Taken": {
            "blurb": "Hi Team,\n\nAs per our checks, no deployment actions were taken on the mentioned date. Please provide us with a snapshot from Seller Central so we can perform a deep dive into the issue."
        },
        "Holiday Revoked & Glitch Corrected": {
            "blurb": "Hi Team\n\nHoliday has been revoked for the requested dates.\nKindly wait for 24 hours to reflect on the portal.\n\nHence Resolving\n\n---\n\nHi Team,\n\ndue to some technical glitch survey was unable to update the MID more than 4 numbers.\nwe have corrected the glitch and shared new survey over email yesterday request you to kindly check and update your working status for upcoming jupiter.\nHence resolving."
        },
        "Holiday Applied & Revoked (Specific Date)": {
            "blurb": "Hi Team\n\nHoliday has been Applied for the requested dates.\nKindly wait for 24 Hours to reflect on the portal.\nAlso, please inform the seller to clear the pipeline orders that will appear on the seller panel before going on holiday and hand them over to the carrier partner.\n\nHence Resolving\n\n---\n\nHi team,\n\nAs per our DD we could see only on 7th Sept we have deployed holiday for this seller as per the request , Holiday has been revoked for 7th Sept 2024.\nKindly wait for some time to reflect on the portal.\n\nHence Resolving"
        },
        "No Response for Correspondence": {
            "blurb": "Hi,\n\nThere is no response for the below correspondence.\nKindly raise a new TT if any issue persists.\n\nHence resolving."
        },
        "September & Future Requests/Technical Issue": {
            "blurb": "Hi Team,\n\nFor any requests other than those for September, we have taken the input. However, please ask the seller to share their final working status in the respective monthly surveys. The holiday will be removed only 7 days prior, as we are awaiting HCP data.\n\nIf this issue persists before the holiday, kindly raise a new TT.\n\n---\n\nHi team,\n\nDue to some technical issue form was not able to register Seller id tomorrow we will be sharing new form to submit the Holiday survey."
        },
        "Seller Raised Holiday - No Access": {
            "blurb": "Hi Team,\n\nAs per our checks we see this is a seller raised holiday and we have no access to seller central to revoke the holiday\nKindly ask the seller to click on edit and remove the holiday.\nThis CTI is used only for Amazon holiday Removals/Applications\n\nResolving this TT"
        },
        "SH Deployed (Specific Dates) - No Revoke": {
            "blurb": "Hi Team,\n\nDue to pickup constraint from Last mile pickup team, SH(Ship Holiday) was deployed for the seller on 04/19 & 04/26\nWe will not be able to revoke the holiday, however rest days we have removed\n\nResolving this TT"
        },
        "SOP Violation - Advanced Request Needed": {
            "blurb": "Hi Team,\nAs per SOP removal/Application request should be raised 2 days in advance from the date requested for removall Application. Thus we will not be revoking/ Deploying the holiday\nPlease follow the SOP going forward\nResolving the case"
        },
        "Holiday Revoked - SOP Note": {
            "blurb": "Hi Team,\n\nHoliday has been revoked for the requested dates.\n\nNote: As per SOP removal request should be raised 2 days in advance from the date requested for removal. So we will be revoking as per the SOP."
        },
        "Confirm Working Status (Jan Survey)": {
            "blurb": "Hi, please ask seller to confirm working status for all dates in Jan in the below survey.\nhttps://amazonexteu.qualtrics.com/jfe/form/SV_emsXUOL6uBt2IRM"
        },
        "Pickup Constraint (Jan-Feb)": {
            "blurb": "Hi Team\n\nPlease note due to pickup constraint on 22nd Jan to 28th Feb the carrier facility will not be operating, requesting you to\nschedule the orders and handover the shipments next day\n\nHence resolving"
        },
        "Holiday Removal (2 Days Before)": {
            "blurb": "Hi team,\nHoliday removal action will be taken 2 days before holiday dates. Hence resolving the sim"
        },
        "Holiday Action Taken - Resolved": {
            "blurb": "Hi team,\nIssue has been resolved. Holiday action has been taken from our end. Kindly wait for 24 hours to reflect on your account.\nHence resolving"
        }
    }
}