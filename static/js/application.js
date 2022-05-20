$(document).ready(function(){
    //connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    //receive details from server
    socket.on('newnumber', function(msg) {
        console.log("Received number" + msg.number);
        numbers_string = '<h2>' + msg.number + '</h2>';
        $('#log').html(numbers_string);
    });

    socket.on('neworder', function(order) {
        console.log("Received number" + order.order);
        numbers_string = '<h2>' + order.order + '</h2>';
        if(order.orderType == "BUY") {
            $('.buy').html(numbers_string);
        } else {
            $('.sell').html(numbers_string);
        }
    });
});