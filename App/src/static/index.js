function openNav() {
    document.getElementById("mySidepanel").style.width = "250px";
}

function closeNav() {
    document.getElementById("mySidepanel").style.width = "0";
}
$(document).ready(function() {
    $("#selectFile").click(function(e) {
        e.preventDefault();
        console.log('function started');
        $.ajax({
            type: "POST",
            contentType: "application/json;charset=utf-8",
            url: `${window.origin}/`,
            traditional: "true",
            data: JSON.stringify('selectFile'),
            dataType: "json"
        });
    });

    $("#pythonImpl").click(function(e) {
        e.preventDefault();
        console.log('function started');
        $.ajax({
            type: "POST",
            contentType: "application/json;charset=utf-8",
            url: `${window.origin}/data`,
            traditional: "true",
            data: JSON.stringify('selectFile'),
            dataType: "json"
        });
    });

});



// function selectFile() {
//     console.log('function started');
//     $.ajax({
//         type: "POST",
//         contentType: "application/json;charset=utf-8",
//         url: `${window.origin}/`,
//         traditional: "true",
//         data: JSON.stringify('elmnt'),
//         dataType: "json"
//         });;
//   };


// fetch(`${window.origin}/`,{
//     method: 'POST',
//     credentials: "include",
//     body: 'message',
//     cache: "no-cache",
//     headers: new Headers({
//         "content-type": "application/json"
//     })
// });