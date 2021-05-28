var app = require('http').createServer(),
    io = require('socket.io')(app, { cors: true });
app.listen(8081,{origins:'*'});
PORT=8081,




io.on('connection',function(socket){
    //获得roomID 和 username
    socket.on('joinRoom',function(data){
        socket.join(data.roomID);
        console.log('socket.id: '+socket.id+', username: '+data.username+', 加入 '+data.roomID+' 房间!')

        socket.username = data.username
        socket.roomID = data.roomID

    })
    socket.on('msg',function(data){
        console.log('socket.roomID: '+socket.roomID)
        io.to(socket.roomID).emit('broadcastMsg',data);
        console.log(JSON.stringify(data)+"发消息了")
    })

})

console.log('listening at :' +PORT)
// 