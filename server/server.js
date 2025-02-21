const { Server } = require('socket.io');

const io = new Server(3000);

const secret = process.env.SERVER_ID

io.on('connection', (socket) => {
    var query = socket.handshake.query;
    var roomid = query.roomid;
    socket.join(roomid);
    console.log('connected', roomid);
    socket.on(secret, (data) => {
        io.to(roomid).emit('webcaption', data);
    });
});