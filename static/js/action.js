document.addEventListener("DOMContentLoaded", function() {
  // Fetch data from the /data/action endpoint
  fetch('/data/action')
    .then(response => response.json())
    .then(data => {
      var tableBody = document.querySelector("table tbody");

      // Clear existing table rows
      tableBody.innerHTML = '';

      if (data.length === 0) {
        // Show green alert if the table is empty
        var alertContainer = document.querySelector(".alert-container");
        alertContainer.innerHTML = `
          <div class="alert alert-dismissible alert-success">
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
            <strong>Good news!</strong> No products out of spec!
          </div>
        `;
        alertContainer.style.display = "block";
      } else {
        // Populate table with data
        data.forEach(item => {
          var row = document.createElement('tr');
          row.classList.add('table-light'); // TABLE ROW COLORS

          // Create cells for each column
          var productCell = document.createElement('th');
          productCell.scope = 'row';
          productCell.textContent = item.Product;

          var compliantCell = document.createElement('td');
          compliantCell.textContent = item.Compliant ? 'Yes' : 'No';

          // Append cells to the row
          row.appendChild(productCell);
          row.appendChild(compliantCell);

          // Append the row to the table body
          tableBody.appendChild(row);
        });

        // Show the red alert if the table has rows
        document.querySelector(".alert-container").innerHTML = `
          <div class="alert alert-dismissible alert-danger">
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
            <strong>Caution:</strong> Following products out of spec!
          </div>
        `;
        document.querySelector(".alert-container").style.display = "block";
      }
    })
    .catch(error => console.error('Error fetching data:', error));
});
