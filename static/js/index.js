
const productName = 'example_product';

// Fetch and insert plot1
fetch(`/api/plot1_html/${productName}`)
.then(response => response.text())
.then(html => {
document.getElementById('plot1').innerHTML = html;
});

// Fetch and insert plot2
fetch(`/api/plot2_html/${productName}`)
.then(response => response.text())
.then(html => {
document.getElementById('plot2').innerHTML = html;
});

// Fetch and insert description
fetch(`/api/description_html/${productName}`)
.then(response => response.text())
.then(html => {
document.getElementById('description').innerHTML = html;
});
