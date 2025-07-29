// Example of options data - can be extended or pulled from the backend dynamically
const stages = {
    "Pickup Related": ["Carrier Controllable", "Seller Controllable", "order status packed up", "Actual Schedule date is Future date / Current Date"],
    "Cancelled orders": ["Customer request cancelled as per SCC", "Orders cancelled for not fulfilling the orders by Seller/TR cancelled"],
    "Holiday": ["Holiday applied before seller raises case","Request yet to taken by the ops", "Holiday Revoking request yet to taken by ops team", "Holiday Revoking request successful","Holiday request on the same day" ],
    "Return and Reimbursement": ["Damaged orders returned back and claiming for the reimbursement"],
	"Address Change and Contact number update": ["New address and updated contact number request"],
	"Technical /Integrator issues": ["Orders not reflecting and Waiting for invoice","NSTS issue"],
	"Amazon controllable tech issue": ["Pickup slot issue"],
	"Activation and Deactivation": ["Activation request","Deactivation request"],
	"Case not actioned": ["Pending Merchant action not actioned"],
	"Duplicate Case": ["Duplicate Case"],
	"POA Cases": ["POA Step 1","POA Step 2", POA Step 3"]
};

function updateStages() {
    const cycle = document.getElementById('cycle').value;
    const stageSelect = document.getElementById('stage');
	const stageDiv = document.getElementById('stageDiv');
    const problemSelect = document.getElementById('problem');
    
    // Reset Stage and Problem dropdowns
    stageSelect.innerHTML = '<option value="">Select Stage</option>';
	problemSelect.innerHTML = '<option value="">Select Problem</option>';
    
    // If a valid cycle is selected, populate the stages dropdown
    if (cycle && stages[cycle]) {
        stages[cycle].forEach(function(stage) {
            const option = document.createElement('option');
            option.value = stage;
            option.textContent = stage;
            stageSelect.appendChild(option);
        });

        // Show the Stage of Issue dropdown after cycle selection
        stageDiv.style.display = 'block';  // Ensure the Stage dropdown is shown
    } else {
        stageDiv.style.display = 'none';  // Hide the Stage dropdown if no valid cycle is selected
    }
}

// Add event listener for cycle selection
document.getElementById('cycle').addEventListener('change', updateStages);