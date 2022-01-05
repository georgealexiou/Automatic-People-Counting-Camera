//function to convert csv string to array of arrays of data
function CSVToArray(data){
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

    while (arrMatches = objPattern.exec(data)){
        var strMatchedDelimiter = arrMatches[1];
        if (
            strMatchedDelimiter.length &&
            strMatchedDelimiter !== delimiter
            ){
            arrData.push( [] );
        }

        var strMatchedValue;

        if (arrMatches[ 2 ]){

            strMatchedValue = arrMatches[ 2 ].replace(
                new RegExp( "\"\"", "g" ),"\"");
        } else 
            strMatchedValue = arrMatches[ 3 ];

        arrData[ arrData.length - 1 ].push( strMatchedValue );
    }

    return( arrData );
}