// Wait for the DOM to be fully loaded
document.addEventListener("DOMContentLoaded", function () {
    // Array containing the days of the week
    const days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'];
    const periods = [1, 2, 3, 4, 5]; // Periods 1 to 5
    const semesters =[1,2,3,4,5,6];

    const scheduleTableBody = document.querySelector("#scheduleTable tbody");

    // Function to generate the table rows
    function generateTable() {
        days.forEach(day => {
            const row = document.createElement("tr");
            row.setAttribute("data-day", day);

            // Add the day as the first cell in the row
            const th = document.createElement("th");
            th.setAttribute("scope", "row");
            th.textContent = day;
            row.appendChild(th);

            // Create period cells
            periods.forEach(period => {
                const td = document.createElement("td");
                const link = document.createElement("a");
                link.href = "#";
                link.setAttribute("data-period", period);
                link.classList.add("btn", "btn-secondary", "open-modal");
                link.textContent = "Add";
                td.appendChild(link);
                row.appendChild(td);
            });

            // Append the row to the table body
            scheduleTableBody.appendChild(row);
        });
    }

    // Call the function to generate the table when the page loads
    generateTable();

    // Modal initialization
    const modal = new bootstrap.Modal(document.getElementById("addSubjectTeacherModal"));

    // Attach click event listeners to buttons
    document.querySelectorAll(".open-modal").forEach(button => {
        button.addEventListener("click", function (event) {
            event.preventDefault();

            // Get the day and period from the clicked button
            const day = this.closest("tr").getAttribute("data-day");
            const period = this.getAttribute("data-period");

            // Get department and year from the table attributes
            const department = document.getElementById("scheduleTable").getAttribute("data-department");
            const year = document.getElementById("scheduleTable").getAttribute("data-sem");

            // Populate modal fields
            document.getElementById("day").value = day;
            document.getElementById("period").value = period;
            document.getElementById("department").value = department;
            document.getElementById("year").value = year;

            // Update the modal title with department and year
            document.getElementById("addSubjectTeacherLabel").textContent = `Time table: ${department} - ${year} semester`;

            // Show the modal
            modal.show();
        });
    });

   
});

document.addEventListener("DOMContentLoaded", function () {
    const modal = new bootstrap.Modal(document.getElementById("addSubjectTeacherModal"));

    // Attach click event listeners to buttons
    document.querySelectorAll(".open-modal").forEach(button => {
        button.addEventListener("click", function (event) {
            event.preventDefault();

            // Get data attributes from the clicked button
            const day = this.getAttribute("data-day");
            const period = this.getAttribute("data-period");
            const subjectId = this.getAttribute("data-subject");
            const teacherId = this.getAttribute("data-teacher");

            // Populate modal fields
            document.getElementById("day").value = day;
            document.getElementById("period").value = period;

            // Pre-select subject if editing
            if (subjectId) {
                document.querySelector('select[name="subject"]').value = subjectId;
            } else {
                document.querySelector('select[name="subject"]').value = "";
            }

            // Pre-select teacher if editing
            if (teacherId) {
                document.querySelector('select[name="TEACHERID"]').value = teacherId;
            } else {
                document.querySelector('select[name="TEACHERID"]').value = "";
            }

            // Update modal title
            const department = document.getElementById("scheduleTable").getAttribute("data-department");
            const year = document.getElementById("scheduleTable").getAttribute("data-sem");
            document.getElementById("addSubjectTeacherLabel").textContent = `Timetable: ${department} - ${year} semester`;

            // Show the modal
            modal.show();
        });
    });
});
