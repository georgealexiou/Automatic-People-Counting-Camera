
// Create root element
// https://www.amcharts.com/docs/v5/getting-started/#Root_element
var root = am5.Root.new("chartdiv");
chart = root.container.children.push(
    am5xy.XYChart.new(root, {})
  );


// Set themes
// https://www.amcharts.com/docs/v5/concepts/themes/
root.setThemes([
  am5themes_Animated.new(root)
]);


// Create chart
// https://www.amcharts.com/docs/v5/charts/xy-chart/
var chart = root.container.children.push(am5xy.XYChart.new(root, {
  panX: true,
  panY: true,
  wheelX: "panX",
  wheelY: "zoomX"
}));


// Add cursor
// https://www.amcharts.com/docs/v5/charts/xy-chart/cursor/
var cursor = chart.set("cursor", am5xy.XYCursor.new(root, {
  behavior: "none"
}));
cursor.lineY.set("visible", false);


// Generate random data
var date = new Date();
date.setHours(0, 0, 0, 0);
var value = 0;

function generatePair(data) {
  value = parseInt(data[1]);
  date = new Date();
  date_raw = data[0].split(":")
  date.setHours(date_raw[0],date_raw[1],date_raw[2], 0)
  return {
    date: date.getTime(),
    value: value
  };
}

function generateData(csvData) {
  var data = [];
  for (var i = 0; i<csvData.length-1; i++) {
    data.push(generatePair(csvData[i]));
  }
  return data;
}


// Create axes
// https://www.amcharts.com/docs/v5/charts/xy-chart/axes/
var xAxis = chart.xAxes.push(am5xy.DateAxis.new(root, {
  maxDeviation: 0.2,
  baseInterval: {
    timeUnit: "second",
    count: 1
  },
  renderer: am5xy.AxisRendererX.new(root, {}),
  tooltip: am5.Tooltip.new(root, {})
}));

var yAxis = chart.yAxes.push(am5xy.ValueAxis.new(root, {
  renderer: am5xy.AxisRendererY.new(root, {})
}));


// Add series
// https://www.amcharts.com/docs/v5/charts/xy-chart/series/
var series = chart.series.push(am5xy.LineSeries.new(root, {
  name: "Series",
  xAxis: xAxis,
  yAxis: yAxis,
  valueYField: "value",
  valueXField: "date",
  tooltip: am5.Tooltip.new(root, {
    labelText: "{valueY}"
  })
}));


// Add scrollbar
// https://www.amcharts.com/docs/v5/charts/xy-chart/scrollbars/
chart.set("scrollbarX", am5.Scrollbar.new(root, {
  orientation: "horizontal"
}));

function updateData(text){

    data = CSVToArray(text);

    var sum = 0;
    for (var i = 0; i < data.length - 1; i++) {
      sum += parseInt(data[i][1]);
    }

    var avg = sum/data.length;
    if (avg>0) {
      document.getElementById("avg_pop").innerHTML = avg;
      document.getElementById("cur_pop").innerHTML = data[data.length - 1][1];
      document.getElementById("status").innerHTML = "Data Found";

      var generated = generateData(data);
      console.log(generated);
      series.data.setAll(generated);

    } else {
      document.getElementById("avg_pop").innerHTML = 0;
      document.getElementById("cur_pop").innerHTML = 0;
      document.getElementById("status").innerHTML = "Data Not Found";
      document.getElementById("status").style.color = "red";
    }

}