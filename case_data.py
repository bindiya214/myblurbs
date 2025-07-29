# case_data.py
Paragon_Cases = {
    "pickup related cases": {
        "carrier controllable": {
            "Carrier delay": {
                "steps": "If the order is still pending for pickup, follow the below step: \n 1. Check the scan time and cross verify the delay scan has been mark from the actual location.\n 2. As a next step escalate the issue to the station team by dropping an escalation email to the concerned station team by Adding Arindom and CRM   in CC and case in APA until the issue get resolved.",
                "status": "Pending Amazon action",
                "blurb": "Dear Seller,\nGreetings from Amazon!\nWe regret the inconvenience caused.\n\nWe have escalated the issue to the respecting Station team and will revert back once we get an update from the station team. \nNote: Your performance won't be affected due to this pickup issue.\nSorry for the Inconvenience caused, we appreciate your understanding and co-operation.\n\nThanks, and Regards.",
                "annotations": "Email has been sent to station and waiting response. \n Subject for the email."
            }
        },
        "seller controllable": {
            "Package not ready": {
                "steps": "If confirmation receive from the station end that packages were not ready from the seller's end and it is a good scan, inform the station team to realign the pickup. \n Revert to the seller, instructing them to keep the packages ready within the slot time, and resolve the case.",
                "status": "Resolve",
                "blurb": "Dear Seller,\nGreetings from Amazon!\nWe regret the inconvenience caused.\n\nWe received an update from the station team that 0 orders missed yesterday due to Packages not being ready from your end. We request you to keep the packages ready during the slot time to avoid the miss in future. \nThanks, and Regards.",
                "annotations": "Received an email confirmation from the station  <b>ABCD <b>  that packages were not ready at the time of Pickup attempt. Hence resolving."
            }
        },
        "Order status picked up.": {
            "Order confirmed picked up": {
                "steps": "Check the ESD and ASD of the order. \n If the order picked on the same ESD and ASD resolve the case. \n If the orders picked up the next day of ESD, please escalate the issue to the station team and inform the team to align the pickup as per ASD date.",
                "status": "Resolve",
                "blurb": "Dear Seller,\nGreetings from Amazon.\nThanks for notifying us.\n\nAs per our checks in internal portal, we see that the order has been processed and shipped successfully. Requesting you to please raise a case for the further issue/issue still persists. Hence resolving the case.\n\nThanks, and Regards.",
                "annotations": "As per PSO dashboard order status stands picked up."
            }
        },
        "Actual Schedule date is Future date / Current Date": {
            "Schedule verification": {
                "steps": "If the Actual Schedule date is a future date please check the ASD and ESD of the orders and resolve the case.",
                "status": "Resolve",
                "blurb": "Dear seller,\n\nGreetings from Amazon!\n\nAs per our checks in internal portal order xxxxx has the Actual Schedule Date of DD/MM/YYYY and pickup will happen accordingly. \nRequesting you to please raise a case if the pickup has not aligned as per Actual schedule date. \nYour Patience and Co-Operation is highly appreciated.\nThanks, and Regards.",
                "annotations": "Pickup will happen as per Actual Schedule Date. "
            }
        }
    },
    "Cancelled orders":{
        "Customer request cancelled as per SCC": {
            "Customer changed mind": {
                "steps": " As per SCC of the orders are cancelled due to SCC please follow the below steps.\n Please check the ASD of the orders and add the order ID’s in the SCC for the pickup status.\n As per SCC if the orders show cancelled please check the time of the orders which got cancelled. \n If the orders cancelled before 11.59PM the current ASD date please resolve the case using the blurb.\n  Add the OID’s for MM",
                "status": "Resolve",
                "blurb": "Dear Seller,\n\nGreetings from Amazon.\nThanks for notifying us.\n\nAs per our checks in internal tool, we see the order has been cancelled for the mentioned location. The order has been cancelled by the customer after it was processed by your end. Kindly add it to your inventory by inbounding.\nNote: Your performance won't be affected due to these cancelled orders.\n\nThanks, and Regards.",
                "annotations": "As per PSO dashboard and SCC order status stands cancelled due to customer request. Metric modification has been provided."
            }
        },
        "Orders cancelled for not fulfilling the orders by Seller/TR cancelled": {
            "Seller unfulfillment": {
                "steps": "Please check the ASD of the orders and add the order ID’s in the SCC for the pickup status. \n As per SCC if the orders show cancelled please check the time of the orders which got cancelled.\n If the orders cancelled post 11.59PM the current ASD date please check why the orders were not fulfilled by the seller and resolve the case using the blurb.  ",
                "status": "Resolve",
                "blurb": "Dear Seller,\n\nGreetings from Amazon.\nThanks for notifying us.\n\nAs per our checks in internal tool, we see the order has been cancelled for the mentioned location. The order has been cancelled for not fulfilling the orders during the slot timings. We request you to keep the packages ready during the slot time and reschedule the orders for the next day to avoid the miss in future. \nThanks, and Regards.",
                "annotations": "As per PSO dashboard and SCC order status stands cancelled due to orders not fulfilled by seller. Hence resolving"
            }
        }
    },
    "Holiday": {
        "Holiday applied before seller raises case ": {
            "Holiday in effect": {
                "steps": "As a first step check with TL whether any deployment taken place for the location for requested date if YES please check the status of the execution and resolve the case. Please cross check whether the holiday has been applied in the smart console.",
                "status": "Resolve",
                "blurb": "Dear Seller,\nGreeting from Amazon!!\nAs per the request, holiday has been applied for the mentioned locations. Requesting you to clear the orders which are fallen before the holiday date to avoid the miss. \nThanks, and Regards.",
                "annotations": "Holiday has been deployed for the mentioned location. Holiday ID: Add the holiday ID"
            }
        },
        "Request yet to taken by the ops": {
            "Holiday request pending": {
                "steps": "If NO, please add the Location ID in the quip for the deployment request and keep the case in PAA until the deployment and execution is successful. \n Please cross check whether the holiday has been applied in the Smart console. ",
                "status": "Pending Amazon action .",
                "blurb": "Dear Seller,\nGreeting from Amazon!!\nAs per the request, holiday request has been raised for the deployment for the mentioned locations. Requesting you to allow us sometime to execute the request. \nThanks, and Regards.",
                "annotations": ""
            }
        },
        "Holiday Revoking request yet to taken by ops team": {
            "Holiday revoke pending": {
                "steps": "Check the holiday date and the reason for revoking the holiday. \n Add Location ID in the quip for the revoke request.",
                "status": "Pending Amazon action .",
                "blurb": "Dear Seller,\nGreeting from Amazon!!\nAs per the request, holiday revoking request has been raised for the mentioned locations. Requesting you to fulfill the orders within the slot time to avoid the miss. \nThanks, and Regards.",
                "annotations": "Holiday revoking request has been raised and awaiting the response."
            }
        },
        "Holiday Revoking request successful": {
            "Holiday revoked": {
                "steps": "Check the holiday revoking execution status and holiday status in the Smart console if the revoking is successful, resolve the case. ",
                "status": "Resolve",
                "blurb": "Dear Seller,\nGreeting from Amazon!!\nAs per the request, holiday revoking request has been successful for the mentioned locations. Requesting you to fulfill the orders within the slot time to avoid the miss. \nThanks, and Regards.",
                "annotations": "Holiday has been revoked for the mentioned location successfully. Holiday ID: "
            }
        },
        "Holiday request on the same day": {
            "Same day holiday request": {
                "steps": "If a seller has raised a holiday request for the same day, inform the seller about the Standard Operating Procedure (SOP) for holidays. \n The SLA for applying a holiday on the Smart Console is 4 days prior to the holiday date. Therefore, we request you to apply for a holiday or raise a case at least 4 days in advance to avoid any issues for upcoming holidays and resolve the case.",
                "status": "Resolve",
                "blurb": "Dear Seller,\nGreeting from Amazon!!\nHoliday request for the mentioned dates will not accepted. The request has been raised on 2/3/2024 on account of Shivaratri and SLA for making holiday on Smart console/requesting for the holiday over case is 4 days prior to the holiday date. Hence, we request you to apply Holiday/ raise case 4 days in advance to avoid the churn for upcoming holidays.\nRequesting you to please arrange the manpower in order to fulfill the orders.\n\nThanks, and Regards.",
                "annotations": "Holiday has not applied for the mentioned location because request was raised on the same day. Hence resolving"
            }
        }
    },
    "Return and Reimbursement ": {
        "Damaged orders returned back and claiming for the reimbursement": {
            "Product damaged and reimbursement claim": {
                "steps": "If a seller encounters issues related to Returns and Reimbursement, such as receiving incorrect products or damaged inventory, and wishes to claim reimbursement for these issues, the case must be transferred to the SESU team. This is because the operations team does not handle return and reimbursement-related queries. Please forward the case to SESU at sesu-in-fba-eom-reg-std-eng-sfl@amazon.in.",
                "status": "Transfer",
                "blurb": "The case has to be annotated and then transferred sesu-in-fba-eom-reg-std-eng-sfl@amazon.in",
                "annotations":"Return and Reimbursement issue, Hence Transferring\", Transfer case to sesu - sesu-in-fba-eom-reg-std-eng-sfl@amazon.in"
            }
        }
    },
    "Address Change and Contact number update": {
        "New address and updated contact number request": {
            "Address update request": {
                "steps": "As and when the seller is located to new business place or the Store POC is changed and the seller raises the concern for the same details are to be added in the quip: https://quip-amazon.com/0rjdA6nh0hk9/MLF-Address-ChangePhone-Number-Update, \n We will add it in the Quip link and resolve the case using Address change blub.",
                "status": "Resolved",
                "blurb": "Dear Seller,\nGreetings from Amazon!\n\nWe have forwarded the request to the concerned team.\nIt may take 7-14 business days to deploy the changes,\nYour co-operation and patience are highly appreciated!\n\nThanks, and Regards.",
                "annotations": "Address change request has been added in the quip.,Quip: https://quip-amazon.com/0rjdA6nh0hk9/MLF-Address-ChangePhone-Number-Update#temp:C:GSd63e5e6f1b83fc7c2d49760b2f"
            }
        }
    },
    "Technical /Integrator issues ": {
        "Orders not reflecting and Waiting for invoice": {
            "Orders not visible/Invoice pending": {
                "steps": "If orders are not reflecting and Waiting for invoice persist identify that the issue lies with the integrator team. Highlight issue to the tech team by raise a ticket to address the integration issue with the specified order IDs. Additionally, inform sellers to reach out to their integrator team for the resolution.Provide ACE for the orders",
                "status": "Resolve",
                "blurb": "Dear Seller,\n\nGreetings from Amazon.\nWe regret the inconvenience caused.\nDue to some technical synchronization constraints in panel the orders were stuck. We have escalated this issue to the technical team and the issue will be resolved soon.\nYour patience and co-operation are highly appreciated\n\nNote: Your performance won't be affected due to this technical issue.\nSorry for the Inconvenience caused, we appreciate your understanding and co-operation.\n\nThanks, and Regards.",
                "annotations": "Issue has been highlighted on the SIM to the Tech team.,SIM: Add SIM link here"
            }
        },
        "NSTS issue": {
            "NSTS error": {
                "steps": "NSTS issue has to be address to the Tech team by raising a SIM. Provide ACE for the orders. ",
                "status": "Resolve",
                "blurb": "Dear Seller,\n\nGreetings from Amazon.\n\nAs this is an integrator tech issue requesting you to raise a case to the integrator team for the resolution. Kindly contact integrator team or Account Manager for assistance.\n\nThanks, and Regards.",
                "annotations": "NSTS Issue has been highlighted on the SIM to the Tech team.,SIM: Add SIM link here"
            }
        }
    },
    "Amazon controllable tech issue": {
        "Pickup slot issue:": {
            "No slots available": {
                "steps": "Request seller for the screenshot the error and examine the error before raising the TT, If the TT has already raised check the status of the TT and resolve the case using the specific blurb. (Provide ACE and MM)",
                "status": "Resolve",
                "blurb": "Dear Seller,\n\nGreetings from Amazon.\nWe regret the inconvenience caused.\n\nDue to pickup/space constraints pickup slot was not available for the below mentioned orders. We have escalated this issue to the technical team and the issue will be resolved soon.\nYour patience and co-operation are highly appreciated,\nNote: Your performance won't be affected due to this technical issue.\nSorry for the Inconvenience caused, we appreciate your understanding and co-operation.\nThanks, and Regards.",
                "annotations": "Pickup slot issue has been highlighted on the SIM to the Tech team.,SIM: Add SIM link here"
            }
        }
    },
    "Activation and Deactivation": {
        "Activation request": {
            "Site suspended due to low performance": {
                "steps": "Please understand the cause of the Activation of the site. If the seller raises case to activate the node is it is suspended for the low performance/fraud activity please resolve the case with the mentioned blurb. ",
                "status": "Pending Merchant Action",
                "blurb": "Dear Seller,\n\nGreetings from Amazon.\n\nAs per checks, we see that site has been deactivated for low performance. Hence activation cannot be performed with the Plan of action. Kindly provide POA in below format:\n 1) Please provide the root causes that led to the issue: \n 2) Please provide the actions you have taken to resolve the issue: \n 3) Please provide steps you have taken to prevent the issue from recurring in the future:\n 4) What is the ETA and escalation metrics followed to resolve the issue:\n 5) Mail confirmation from integration tech. team to attached for validation (If there was any technical issue from integrator's end),",
                "annotations": "Awaiting the response from the Brand to provide Plan of action."
            },
            "Activation request raised": {
                "steps": "If the site has been deactivated based on the seller request then request will be taken into consideration and need to add the internal paragon quip and activation SIM: https://t.corp.amazon.com/D70505988/communication. Do not resolve the case until the site is activated",
                "status": "Pending Amazon action .",
                "blurb": "Dear Seller,\n\nGreetings from Amazon!\n\nAs per the request below, Location has been added for the reactivation. We will provide a confirmation on the account active status.  \n\nThanks, and Regards.",
                "annotations": "Activation request has been added on the activation SIM: https://t.corp.amazon.com/D70505988/communication,"
            },
            "Activation request is complete": {
                "steps": "Once the site is activated, please resolve the case by adding the details in the quip. ",
                "status": "Resolve",
                "blurb": "Dear Seller,\n\nGreetings from Amazon!\n\nAs per the request below, Location has been reactivated.\nRequesting you to please check on the account active status and do raise a case if there are any issue persists.\n\nThanks, and Regards.",
                "annotations": "Activation request is successful hence resolving"
            }
        },
        "Deactivation request": {
            "Deactivation request raised": {
                "steps": "Please cross check the date from when the site has to get deactivated and add the same in the internal paragon quip and also in the Deactivation quip: https://t.corp.amazon.com/D70505370/communication ",
                "status": "Pending Amazon action .",
                "blurb": "Dear Seller,\n\nGreetings from Amazon!\n\nAs per the request below, Location has been added for the deactivated. We will provide a confirmation on the account status. \n\nThanks, and Regards.",
                "annotations": "Deactivation request has been added on the activation SIM: https://t.corp.amazon.com/D70505370/communication"
            },
            "Deactivation request is complete": {
                "steps": "Once the site is deactivated, please resolve the case by adding the details in the quip.",
                "status": "Resolve",
                "blurb": "Dear Seller,\n\nGreetings from Amazon!\n\nAs per the request below, Location has been deactivated.\nRequesting you to please check on the account active status and do raise a case if there are any issue persists.\n\nThanks, and Regards.",
                "annotations": "Deactivation request is successful hence resolving"
            }
        }
    },
    "Case not actioned": {
        "Pending Merchant action not actioned": {
            "Seller not responding after 48 hours": {
                "steps": "In Any case if we need data and inputs from seller for the raised case, we revert on the case to share the details, if in case seller has not shared the data, we wait until 48 hrs. if no action has been taken then we will be resolving case using pending merchant action blurb.",
                "status": "Resolve",
                "blurb": "Dear Seller,\nGreetings from Amazon!\n\nAs there is no response for two days hope the issue is resolved.\nHence resolving the case.\nKindly raise a fresh case if issue persist.\n\nThanks, and Regards.",
                "annotations": "No response form seller >48 hours,"
            }
        }
    },
    "Duplicate Case": {
        "Duplicate Case": {
            "Identical case found": {
                "steps": "If a seller has raised a duplicate case, inform the seller that they have submitted a duplicate case. Merge the new case ID with the existing case ID and resolve the duplicate case.",
                "status": "Resolve",
                "blurb": "Dear Seller,\n\nGreetings from Amazon!\n\nWe have noticed that you have created multiple contacts for the same concern. To avoid duplication and delay in response, I am merging this case ID: 5593549362 into the existing case ID: 5597419612.\nPlease refer to this existing case ID for any future correspondence on this issue, and use the customized case URL of that case for contacting about this issue.\n\nYour customized case URL for case # 5597419612: https://paragon-eu.amazon.com/hz/view-case?caseId=5597419612\n\nThanks, and Regards.",
                "annotations": "Resolving the case has Duplicate. Following case ID: Add the existing case ID here"
            }
        }
    },
    "POA Cases": {
        "POA step 1 ": {
            "Sharing POA format": {
                "steps": "When site is suspended by Amazon end due to Scheduling/Handover miss, seller has to raise a case by sharing the POA with the followed question. ",
                "status": "Pending Merchant action",
                "blurb": "Dear Seller,\nGreetings from Amazon!\n\nKindly provide POA in below format,\n1.) Please provide the root causes that led to the issue: \n2.) Please provide the actions you have taken to resolve the issue: \n3.) Please provide steps you have taken to prevent the issue from recurring in the future:\n4.) What is the ETA and escalation metrics followed to resolve the issue:\n5.) Mail confirmation from integration tech. team to attached for validation (If there was any technical issue from integrator's end),",
                "annotations": "POA format has been shared to the seller and awaiting the response."
            }
        },
        "POA Step 2": {
            "POA review (POA meets criteria) ": {
                "steps": "Associate need to do level 1 check as mention in SOP before sending the POA for next level review",
                "status": "Pending Amazon action",
                "blurb": "Dear Seller, \n\nGreetings from Amazon! \n\nThank you for sharing the Plan of Action. \n\nWe have shared the POA for review to the concerned team and will soon get back to you with updates. \n\nYour patience is greatly appreciated.",
                "annotations": "POA has sent for the approval, awaiting response for the same. "
            }
        },
        "POA Step 3": {
            "POA Approved": {
                "steps": "POA shared by the seller is meeting the expectation when case has to resolved by activating the site. Educate the seller not to repeat the instance of miss in future. ",
                "status": "Resolved",
                "blurb": "Dear Seller, \n\nGreetings from Amazon! \n\nThank you for sharing the Plan of Action. \n\nWe acknowledge the Plan of Action shared by you. Your store will be activated ASAP.\n\nKindly process the orders in timely manner and maintain the quality of shipments to avoid such instances in future.\n\nAppreciate your patience. \n\nRegards,",
                "annotations": "POA is approved and site is activated"
            }
        }
    },
    "Transfer case ": {
        "Case needs transfer": {
            "Incorrect team assignment": {
                "steps": "As per checks we see this site belong to SIWI,hence transferring to tam-sf-operations ",
                "status": "",
                "blurb": "sesu-in-fba-eom-reg-std-eng-sfl@amazon.in",
                "annotations": "sesu-in-fba-eom-reg-std-eng-sfl@amazon.in,\"As per our checks, we see this site doesn't belong to MLF, hence transferring.\""
            }
        }
    }
}