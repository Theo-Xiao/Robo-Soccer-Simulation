import SocketCommunicator as Socket


def Forward(name):
    Socket.noReply(name + ",moveForward(100)")
    print(name + ",moveForward(100)")


def Right(name):
    Socket.noReply(name + ",moveRight(-100)")
    print(name + ",moveRight(-100)")


def Left(name):
    Socket.noReply(name + ",moveRight(100)")
    print(name + ",moveRight(100)")


def Backward(name):
    Socket.noReply(name + ",moveForward(-100)")
    print(name + ",moveForward(-100)")


def SpinR(name):
    Socket.noReply(name + ",spin(100)")
    print(name + ",spin(100)")


def SpinL(name):
    Socket.noReply(name + ",spin(-100)")
    print(name + ",spin(-100)")


def Suck(name):
    Socket.noReply(name + ",setSuction(-100)")
    print(name + ",setSuction(-100)")


def Expel(name):
    Socket.noReply(name + ",setSuction(100)")
    print(name + ",setSuction(100)")


def Stop(name):
    Socket.noReply(name + ",stop()")
    print(name + ",stop()")


def SpinStop(name):
    Socket.noReply(name + ",spin(0)")
    print(name + ",spin(0)")


# def Send(msg):
#     print("sent: " + msg)
#     return Socket.send(msg)
