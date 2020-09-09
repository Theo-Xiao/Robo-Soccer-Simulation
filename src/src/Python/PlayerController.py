import SocketCommunicator as Socket
import PlayerCommands as Player
import time


def getXZ(data):
    new = data.replace(";", " ")
    new = new.replace(",", " ")
    # if "'b" in new:
    #     new = new.replace("'b", " ")

    new = new.split(" ")
    print(new)
    return new[1], new[2]


def get_angle(data):
    new = data.replace(";", " ")
    new = new.replace(",", " ")
    new = new.split(" ")
    return new[1]


def PlayerController():
    playerPosition = "player2,GPS()"
    ballPosition = "ball,GPS()"
    blueplayerPosition = "player1,GPS()"
    last_good_angle = 270

    try:
        xz_old = getXZ((Socket.send(playerPosition))[2:-3])
        x_old = float(xz_old[0])
        z_old = float(xz_old[1])
        spinning = False
        while True:
            bxz = getXZ("ball," + str(Socket.send(ballPosition))[2:-3])
            time.sleep(.20)
            bxz2 = getXZ("ball," + str(Socket.send(ballPosition))[2:-3])
            xz = getXZ(str(Socket.send(playerPosition))[2:-3])
            bx = float(bxz[0])
            bz = float(bxz[1])

            x = float(xz[0])
            z = float(xz[1])
            # print(x)
            dx = float(x - x_old)
            dz = float(z - z_old)

            x_old = x
            z_old = z
            if dx == 0 and dz == 0:
                Player.Backward(playername)
                # Player.Backward(playername)
                time.sleep(3)
            else:
                # we only care about the third component of cross product
                cross_3 = float(dx * (bz - z) - dz * (bx - x))
                if cross_3 == 0:
                    # 0 or 180 degree
                    print("0 or 180 degree")
                    dot = float(x * bx + z * bz)
                    if dot > 0:
                        Player.SpinStop(playername)
                        spinning = False
                    elif dot < 0:
                        # if not already spinning
                        if not spinning:
                            Player.SpinR(playername)
                elif cross_3 > 0:
                    # print("left")
                    Player.SpinL(playername)
                    spinning = True
                elif cross_3 < 0:
                    # print("right")
                    Player.SpinR(playername)
                    spinning = True

                if spinning:
                    time.sleep(.110)
                    spinning = False
                    Player.SpinStop(playername)

                Player.Forward(playername)
                time.sleep(.20)
                Player.Suck(playername)
                Player.Suck(playername)
            time.sleep(.100)

    except:
        cur_angle = float(get_angle(Socket.send("player2,getCompass()")[2:-3]))
        angle_Spin(cur_angle)
        moveTo(-20, 0)
        Player.Expel(playername)
        # Player.Forward(playername)
        # time.sleep(8)
        # Player.Stop(playername)
        # moveTo(-40, 0)

        # Player.Backward(playername)
        # time.sleep(.30)
        # Player.Stop(playername)
        # bxz = getXZ("ball," + str(Socket.send(ballPosition))[2:-3])
        # if "Possesion" not in bxz:
        #     bxz = getXZ("ball," + str(Socket.send(ballPosition))[2:-3])
        #     if "player 2" not in bxz and "Possesion" not in bxz:
        #         time.sleep(1)
        #     try:
        #         xz = getXZ(str(Socket.send(playerPosition))[2:-3])
        #         bxz = getXZ("ball," + str(Socket.send(ballPosition))[2:-3])
        #         bx = float(bxz[0])
        #         bz = float(bxz[1])
        #         x = float(xz[0])
        #         z = float(xz[1])
        #         if abs(bx - x) > 1 and abs(bz - z) > 1:
        #             print(bx, x)
        #             PlayerController()
        #         else:
        #             cur_angle = float(get_angle(Socket.send("player2,getCompass()")[2:-3]))
        #             angle_Spin(cur_angle)
        #             moveTo(-40, 0)
        #             Player.Expel()


def moveForward(x):
    Socket.noReply("player2,moveForward(" + str(x) + ")")


def moveRight(x):
    Socket.noReply("player2,moveRight(" + str(x) + ")")


# def angle_Spin(cur_angle):
#     while not (190 > cur_angle > 180):
#         try:
#             Player.SpinR(playername)
#             time.sleep(.100)
#             Player.Stop(playername)
#             time.sleep(.30)
#             cur_angle = float(get_angle(Socket.send("player2,getCompass()")[2:-3]))
#         except:
#             # print(cur_angle)
#             pass

def angle_Spin(angle):
    compass = Socket.send("player2,getCompass()")
    # print("compass length: " + len(compass))
    while len(compass) < 20:
        compass = Socket.send("player2,getCompass()")
        # print("compass length: " + len(compass))
    
        print("Compass---" + compass)
    cur_angle = float(get_angle(Socket.send("player2,getCompass()")[2:-3]))
    while not((angle + 5) > cur_angle > (angle - 5)):

        if cur_angle <= angle:
            Player.SpinR(playername)
            time.sleep(100)
            Player.Stop(playername)
    
        elif cur_angle > angle:
            Player.SpinL(playername)
            time.sleep(100)
            Player.Stop(playername)
    
        time.sleep(20)
        compass = Socket.send("player2,getCompass()")
        # print("compass length: " + len(compass))
        while len(compass) > 26:
            compass = Socket.send("player2,getCompass()")
            # print("compass length: " + len(compass))

            print("Compass---" + compass)
            cur_angle = float(get_angle(Socket.send("player2,getCompass()")[2:-3]))










def moveTo(x, z):
    try:
        xFlag = False
        zFlag = False
        xprev = 0.0
        zprev = 0.0
        ret_mess = getXZ((Socket.send(playerPosition))[2:-3])
        print(ret_mess)
        xPos = float(ret_mess[0])
        zPos = float(ret_mess[1])
        xdir = 1
        zdir = 1
        if round(xPos) < x:
            xdir = -1
        if round(zPos) < z:
            zdir = -1
        if round(xPos) == x or abs(round(xPos) - x) < 2:
            xdir = 0
        if round(zPos) == z or abs(round(zPos) - z) < 2:
            zdir = 0

        moveForward(3000 * xdir)
        moveRight(3000 * zdir)

        while not xFlag or not zFlag:
            if abs(float(xPos) - float(x)) < 1 and not xFlag:
                Player.Stop(playername)
                xFlag = True
            if abs(float(zPos) - float(z)) < 1 and not zFlag:
                Player.Stop(playername)
                zFlag = True
            if xPos == xprev and abs(float(xPos) - float(x)) > 1:
                Player.Stop(playername)
                moveForward(100 * xdir)
            if zPos == zprev and abs(float(zPos) - float(z)) > 1:
                Player.Stop(playername)
                moveRight(100 * zdir)

            time.sleep(.100)
            ret_mess = getXZ((Socket.send(playerPosition))[2:-3])
            xprev = xPos
            zprev = zPos
            xPos = ret_mess[0]
            zPos = ret_mess[1]
    except:
        moveTo(x, z)


def main():
    IP = "127.0.0.1"
    roverPort = 9003
    global playername
    global playerPosition
    playername = "player2"
    playerPosition = "player2,GPS()"
    try:
        Socket.connectToServer(IP, roverPort)
        # moveTo(-20, 0)
        # cur_angle = float(get_angle(Socket.send("player2,getCompass()")[2:-3]))
        # angle_Spin(cur_angle)
        PlayerController()
    except OSError as error:
        print(error)


main()
