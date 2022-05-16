$(document).ready(function(){
    //connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    //receive details from server
    socket.on('newnumber', function(msg) {
        console.log("Received number" + msg.number);
        numbers_string = '<p>' + msg.number + '</p>';
        $('#log').html(numbers_string);
    });

});