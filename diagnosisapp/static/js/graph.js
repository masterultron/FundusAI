var barChartData = {
labels: [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
],
datasets: [
    {
    label: "Water",
    backgroundColor: "#0E45B7F2",
    borderColor: "blue",
    borderWidth: 1,
    data: [41, 30, 12, 14, 30, 0, 50, 29, 37, 10]
    },
    {
    label: "Steps",
    backgroundColor: "#FFC700",
    borderColor: "orange",
    borderWidth: 1,
    data: [12, 0, 0, 28, 0, 18, 0, 21, 0, 5.1]
    },
    {
    label: "Calories",
    backgroundColor: "#71DDB1",
    borderColor: "green",
    borderWidth: 1,
    data: [23, 15, 5, 21, 21, 9.5, 22, 8, 21, 0]
    },
]
};

var chartOptions = {
responsive: true,
legend: {
    position: 'right'
},
title: {
    display: true,
    text: "Testing Activity",
    position: 'left'
},
scales: {
    yAxes: [{
    ticks: {
        beginAtZero: false
    }
    }]
},
}

window.onload = function() {
var ctx = document.getElementById("canvas").getContext("2d");
window.myBar = new Chart(ctx, {
    type: "bar",
    data: barChartData,
    options: chartOptions
});
};

