# easyship_data.py

Easyship_Cases = {
    "Amazon Controllable": {
        "If Order is in cancelled state": {
            "blurb": "Hi Team,\n\n As per the trail mail, the order with Order ID: [Order ID] for seller [Seller Name] stands cancelled.\n\nUpon checking SCC, we observed bad scans which indicate a pickup miss from the Last Mile team, leading to the customer cancelling the order.\n\nRequesting LM to kindly review and share preventive actions to avoid such occurrences going forward.\n\nHence resolving.\n\nRegards,\n[Your Name / Team]"
        },
        "If Order is pending or yet to be picked.": {
            "blurb": "Hi Team,\n\nThe order with Order ID: [Order ID] for seller [Seller Name] is yet to be picked up as per the trail mail.\n\nOn checking SCC, we noticed a bad scan event which could lead to potential customer dissatisfaction and cancellation if not addressed on time.\n\nRequesting the LM team to kindly align the pickup on priority to avoid escalation.\n\nHence resolving.\n\nRegards,\n[Your Name / Team]"
        },
        "If Manifested State/Scheduled for pickup.": {
            "blurb": "Hi Team,\n\nAs per SCC, the order with Order ID: [Order ID] for seller [Seller Name] is in manifested state with pickup scheduled for [Scheduled Date].\n\nRequesting the LM team to ensure pickup is aligned without fail to avoid any further delays.\n\nKindly align the pickup on priority.\n\nHence resolving.\n\nRegards,\n[Your Name / Team]"
        }
    },
    "Seller controllable": {
        "Pending Pickup": {
            "blurb": "Hi Team,\n\nAs per the current status, the order with Order ID: [Order ID] for seller [Seller Name] is pending due to handover delay.\n\nSeller has been contacted and advised to complete the handover at the earliest. Request LM team to realign pickup based on seller’s availability.\n\nHence resolving.\n\nRegards,\n[Your Name / Team]"
        },
        "If Order is pending or yet to be picked.": { # Renamed this to avoid confusion with the previous one, assuming this is for 'cancelled due to non-handover'
            "blurb": "Hi Team,\n\nAs per the trail communication, Order ID: [Order ID] for seller [Seller Name] got cancelled due to non-handover.\n\nWe have reached out to the seller and explained how such cancellations directly impact their account metrics and customer trust. They have been advised to take timely action for future shipments.\n\nHence resolving.\n\nRegards,\n[Your Name / Team]"
        }
    }
}