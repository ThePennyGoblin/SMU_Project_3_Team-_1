document.addEventListener("DOMContentLoaded", function() {
    // Utility function to sort data by "Pct In Spec"
    function sortByPctInSpec(data, pctKey) {
      return data.sort((a, b) => {
        let aValue = parseFloat(a[pctKey].replace('%', ''));
        let bValue = parseFloat(b[pctKey].replace('%', ''));
        return aValue - bValue;
      });
    }
  
    // Utility function to format values with appropriate precision
    function formatValue(value, decimals = 2) {
      return parseFloat(value).toFixed(decimals);
    }
  
    // Fetch and populate Weight data
    fetch('/data/overview/weight')
      .then(response => response.json())
      .then(data => {
        var tableBody = document.querySelector("#weightSection tbody");
        tableBody.innerHTML = '';
  
        sortByPctInSpec(data, 'Pct In Spec Weight').forEach((item, index) => {
          var row = document.createElement('tr');
          row.classList.add(index % 2 === 0 ? 'table-light' : 'table-secondary');
  
          var productCell = document.createElement('th');
          productCell.scope = 'row';
          productCell.textContent = item.Product;
  
          var countCell = document.createElement('td');
          countCell.textContent = item.Count; // Ensure this field is correct
  
          var minWeightCell = document.createElement('td');
          minWeightCell.textContent = formatValue(item['Min Weight']);
  
          var maxWeightCell = document.createElement('td');
          maxWeightCell.textContent = formatValue(item['Max Weight']);
  
          var avgWeightCell = document.createElement('td');
          avgWeightCell.textContent = formatValue(item['Average Weight']);
  
          var pctInSpecCell = document.createElement('td');
          pctInSpecCell.textContent = item['Pct In Spec Weight']; // Ensure this field is correct
  
          var countOffspecCell = document.createElement('td');
          countOffspecCell.textContent = item['Count Offspec'];
  
          var compliantCell = document.createElement('td');
          compliantCell.textContent = item.Compliant ? 'Yes' : 'No';
  
          row.appendChild(productCell);
          row.appendChild(countCell);
          row.appendChild(minWeightCell);
          row.appendChild(maxWeightCell);
          row.appendChild(avgWeightCell);
          row.appendChild(pctInSpecCell);
          row.appendChild(countOffspecCell);
          row.appendChild(compliantCell);
  
          tableBody.appendChild(row);
        });
      })
      .catch(error => console.error('Error fetching weight data:', error));
  
    // Fetch and populate Height data
    fetch('/data/overview/height')
      .then(response => response.json())
      .then(data => {
        var tableBody = document.querySelector("#heightSection tbody");
        tableBody.innerHTML = '';
  
        sortByPctInSpec(data, 'Pct In Spec Height').forEach((item, index) => {
          var row = document.createElement('tr');
          row.classList.add(index % 2 === 0 ? 'table-light' : 'table-secondary');
  
          var productCell = document.createElement('th');
          productCell.scope = 'row';
          productCell.textContent = item.Product;
  
          var countCell = document.createElement('td');
          countCell.textContent = item.Count_Height; // Ensure this field is correct
  
          var minHeightCell = document.createElement('td');
          minHeightCell.textContent = formatValue(item['Min Height']);
  
          var maxHeightCell = document.createElement('td');
          maxHeightCell.textContent = formatValue(item['Max Height']);
  
          var avgHeightCell = document.createElement('td');
          avgHeightCell.textContent = formatValue(item['Average Height']);
  
          var pctInSpecCell = document.createElement('td');
          pctInSpecCell.textContent = item['Pct In Spec Height']; // Ensure this field is correct
  
          var countOffspecCell = document.createElement('td');
          countOffspecCell.textContent = item['Count Offspec'];
  
          var compliantCell = document.createElement('td');
          compliantCell.textContent = item.Compliant ? 'Yes' : 'No';
  
          row.appendChild(productCell);
          row.appendChild(countCell);
          row.appendChild(minHeightCell);
          row.appendChild(maxHeightCell);
          row.appendChild(avgHeightCell);
          row.appendChild(pctInSpecCell);
          row.appendChild(countOffspecCell);
          row.appendChild(compliantCell);
  
          tableBody.appendChild(row);
        });
      })
      .catch(error => console.error('Error fetching height data:', error));
  
    // Scroll-to functionality
    document.querySelectorAll('.scroll-to').forEach(button => {
      button.addEventListener('click', function(event) {
        event.preventDefault();
        const targetId = this.getAttribute('href');
        document.querySelector(targetId).scrollIntoView({ behavior: 'smooth' });
      });
    });
  });
  