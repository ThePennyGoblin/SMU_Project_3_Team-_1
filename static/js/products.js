document.addEventListener("DOMContentLoaded", function() {
    fetch('/data/products/list')
      .then(response => response.json())
      .then(products => {
        console.log("Product list data: ", products); // Log product list data
        const productList = document.getElementById('product-list');
        productList.innerHTML = '';
  
        products.forEach(product => {
          const listItem = document.createElement('li');
          listItem.className = 'list-group-item';
          listItem.textContent = product.product_name;
          listItem.addEventListener('click', () => loadProductData(product.product_name));
          productList.appendChild(listItem);
        });
  
        const defaultProduct = products[0].product_name;
        console.log("Default product: ", defaultProduct); // Log default product
        loadProductData(defaultProduct);
      })
      .catch(error => console.error('Error fetching product list:', error));
  });
  
  function loadProductData(product) {
    console.log("Selected product: ", product); // Log the selected product
    const encodedProduct = encodeURIComponent(product);
    console.log("Encoded product: ", encodedProduct); // Log the encoded product
  
    // Fetch and render the weight plot
    fetch(`/data/products/plot/weight/${encodedProduct}`)
      .then(response => response.text())
      .then(plotHtml => {
        console.log("Weight plot HTML: ", plotHtml); // Log the weight plot HTML
        document.getElementById('chart1').innerHTML = plotHtml;
        executeScripts(document.getElementById('chart1'));
      })
      .catch(error => console.error('Error fetching weight plot:', error));
  
    // Fetch and render the height plot
    fetch(`/data/products/plot/height/${encodedProduct}`)
      .then(response => response.text())
      .then(plotHtml => {
        console.log("Height plot HTML: ", plotHtml); // Log the height plot HTML
        document.getElementById('chart2').innerHTML = plotHtml;
        executeScripts(document.getElementById('chart2'));
      })
      .catch(error => console.error('Error fetching height plot:', error));
  
    // Fetch and render the weight statistics
    fetch(`/data/products/describe/weight/${encodedProduct}`)
      .then(response => response.json())
      .then(data => {
        console.log("Weight description response: ", data); // Log the weight description response
        const statsWeightBody = document.getElementById('stats-weight');
        statsWeightBody.innerHTML = '';
  
        if (data.length > 0) {
          const item = data[0];
          const keys = ['Average', 'Compliant', 'Count', 'Count Offspec', 'Max', 'Min', 'Pct In Spec', 'Product'];
          keys.forEach(key => {
            const row = document.createElement('tr');
            row.classList.add('table-light');
  
            const keyCell = document.createElement('th');
            keyCell.scope = 'row';
            keyCell.textContent = key;
  
            const valueCell = document.createElement('td');
            valueCell.textContent = item[key];
  
            row.appendChild(keyCell);
            row.appendChild(valueCell);
            statsWeightBody.appendChild(row);
          });
        }
      })
      .catch(error => console.error('Error fetching weight statistics:', error));
  
    // Fetch and render the height statistics
    fetch(`/data/products/describe/height/${encodedProduct}`)
      .then(response => response.json())
      .then(data => {
        console.log("Height description response: ", data); // Log the height description response
        const statsHeightBody = document.getElementById('stats-height');
        statsHeightBody.innerHTML = '';
  
        if (data.length > 0) {
          const item = data[0];
          const keys = ['Average', 'Compliant', 'Count', 'Count Offspec', 'Max', 'Min', 'Pct In Spec', 'Product'];
          keys.forEach(key => {
            const row = document.createElement('tr');
            row.classList.add('table-light');
  
            const keyCell = document.createElement('th');
            keyCell.scope = 'row';
            keyCell.textContent = key;
  
            const valueCell = document.createElement('td');
            valueCell.textContent = item[key];
  
            row.appendChild(keyCell);
            row.appendChild(valueCell);
            statsHeightBody.appendChild(row);
          });
        }
      })
      .catch(error => console.error('Error fetching height statistics:', error));
  }
  
  function executeScripts(element) {
    const scripts = element.getElementsByTagName('script');
    for (let i = 0; i < scripts.length; i++) {
      const script = document.createElement('script');
      script.type = scripts[i].type || 'text/javascript';
      if (scripts[i].src) {
        script.src = scripts[i].src;
      } else {
        script.textContent = scripts[i].textContent;
      }
      document.head.appendChild(script);
    }
  }
  