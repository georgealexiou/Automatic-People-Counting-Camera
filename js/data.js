//returns todays date in dd_mm_yyyy format
function formatDate() {
    var today = new Date();
    var dd = String(today.getDate()).padStart(2, '0');
    var mm = String(today.getMonth() + 1).padStart(2, '0');
    var yyyy = today.getFullYear();

    today = dd + '_' + mm + '_' + yyyy;

    return today
}

function getData(today) {
    fetch('./data/' + today + '.csv')
        .then(response => response.text())
        .then(data => {
            return CSVToArray(data);
        });

        return ("");
}

function readSingleFile(e) {
    var file = e.target.files[0];
    if (!file) {
        return;
    }
    var reader = new FileReader();
    reader.onload = function (e) {
        var contents = e.target.result;
        displayContents(contents);
    };
    reader.readAsText(file);
}

//function to convert csv string to array of arrays of data
function CSVToArray(data) {
    const delimiter = ",";
    var objPattern = new RegExp(
        (
            "(\\" + delimiter + "|\\r?\\n|\\r|^)" +
            "(?:\"([^\"]*(?:\"\"[^\"]*)*)\"|" +
            "([^\"\\" + delimiter + "\\r\\n]*))"
        ),
        "gi"
    );

    var arrData = [[]];
    var arrMatches = null;

    while (arrMatches = objPattern.exec(data)) {
        var strMatchedDelimiter = arrMatches[1];
        if (
            strMatchedDelimiter.length &&
            strMatchedDelimiter !== delimiter
        ) {
            arrData.push([]);
        }

        var strMatchedValue;

        if (arrMatches[2]) {

            strMatchedValue = arrMatches[2].replace(
                new RegExp("\"\"", "g"), "\"");
        } else
            strMatchedValue = arrMatches[3];

        arrData[arrData.length - 1].push(strMatchedValue);
    }

    return (arrData);
}