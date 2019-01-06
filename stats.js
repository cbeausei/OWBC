var table;

function write() {
  var n = document.getElementById('select').value;
  var list =  document.getElementById('list');
  while (list.children.length > 1) {
    list.children[1].remove();
  }
  table[n].value.forEach(function(row_stat) {
    var row = document.createElement('tr');
    var cellType = 'th';
    var mean = row_stat[row_stat.length - 1];
    row_stat.forEach(function(cell_stat) {
      var cell = document.createElement(cellType);
      cell.innerHTML = cell_stat;
      if (mean != 'N/A' && cell_stat != 'N/A' && cellType != 'th') {
        var perf = cell_stat / mean;
        var red, green;
        if (perf > 2) perf = 2;
        if (perf < 0) perf = 0;
        if (perf > 1) {
          green = 255;
          red = 255 * (2 - perf);
        }
        else {
          red = 255;
          green = 255 * perf;
        }
        cell.setAttribute('style', 'background-color: rgba(' + red + ', ' + green + ', 0, 1)');
      }
      cellType = 'td';
      row.appendChild(cell);
    });
    list.appendChild(row);
  });
}

$.getJSON('table.json', function(json) {
  table = json;
  var i = 0;
  var select = document.getElementById('select');
  table.forEach(function(stat_type) {
    var opt = document.createElement('option');
    opt.value = i;
    opt.innerHTML = stat_type.key;
    select.appendChild(opt);
    i += 1;
  });
  write();
});

function changed() {
  write();
}
