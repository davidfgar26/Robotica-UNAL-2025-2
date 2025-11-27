import rclpy
from rclpy.node import Node
from turtlesim.srv import TeleportAbsolute, TeleportRelative, SetPen
import sys, tty, termios, select

# --------- LECTURA DE TECLAS ----------
def get_key():
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_controller')

        self.teleport_abs = self.create_client(TeleportAbsolute, '/turtle1/teleport_absolute')
        self.teleport_rel = self.create_client(TeleportRelative, '/turtle1/teleport_relative')
        self.pen         = self.create_client(SetPen, '/turtle1/set_pen')

        self.get_logger().info("Esperando servicios...")
        for c in [self.teleport_abs, self.teleport_rel, self.pen]:
            while not c.wait_for_service(timeout_sec=1.0):
                self.get_logger().info(" Esperando servicio...")

        # tamaño de letras
        self.h = 2.2
        self.w = 1.2

        # posiciones
        self.positions = {
            'L': (2, 8),
            'N': (5, 8),
            'F': (8, 8),
            'D': (2, 4),
            'G': (5, 4),
            'P': (8, 4),
        }

        # movimiento  flechas
        self.step = 0.5
        self.turn = 0.5

        self.get_logger().info("\n=== CONTROL ===")
        self.get_logger().info("Flechas: mover")
        self.get_logger().info("Letras: N F L D G P")
        self.get_logger().info("Q: salir\n")

    # --------- Pen ----------
    def set_pen(self, r, g, b, width, off):
        req = SetPen.Request()
        req.r = r
        req.g = g
        req.b = b
        req.width = width
        req.off = off
        fut = self.pen.call_async(req)
        rclpy.spin_until_future_complete(self, fut)

    # --------- Movimientos ----------
    def teleport(self, x, y, th=0):
        req = TeleportAbsolute.Request()
        req.x = float(x)
        req.y = float(y)
        req.theta = float(th)
        fut = self.teleport_abs.call_async(req)
        rclpy.spin_until_future_complete(self, fut)

    def move_relative(self, lin, ang):
        req = TeleportRelative.Request()
        req.linear = float(lin)
        req.angular = float(ang)
        fut = self.teleport_rel.call_async(req)
        rclpy.spin_until_future_complete(self, fut)

    # --------- Dibujado ----------
    def draw_by_points(self, pts, pen_color, pen_width):

        # apaga lápiz
        self.set_pen(0,0,0,pen_width,True)

        # primer punto
        x0,y0,th0 = pts[0]
        self.teleport(x0,y0,th0)

        # enciende lápiz
        r,g,b = pen_color
        self.set_pen(r,g,b,pen_width,False)

        # trazar
        for x,y,th in pts[1:]:
            self.teleport(x,y,th)

        self.set_pen(0,0,0,pen_width,True)

    # --------- Letras ----------

    def draw_L(self):
        bx,by = self.positions["L"]
        h,w = self.h,self.w
        pts = [
            (bx, by+h, 0),
            (bx, by, 0),
            (bx+w, by, 0)
        ]
        self.draw_by_points(pts, (0,0,255), 3)

    def draw_N(self):
        bx, by = self.positions['N']
        h, w = self.h, self.w

        pts = [
            (bx, by, 0),          
            (bx, by + h, 0),       
            (bx + w, by, 0),       
            (bx + w, by + h, 0)    
        ]

        self.draw_by_points(pts, pen_color=(255, 0, 0), pen_width=3)


    def draw_F(self):
        bx, by = self.positions['F']
        h, w = self.h, self.w
        pts = [
            (bx, by, 0),             
            (bx, by + h, 0),           
            (bx + w, by + h, 0),       
            (bx, by + h, 0),           
            (bx, by + h * 0.5, 0),    
            (bx + w * 0.6, by + h * 0.5, 0)  
        ]

        self.draw_by_points(pts, pen_color=(0, 128, 0), pen_width=4)


    def draw_D(self):
        bx,by = self.positions["D"]
        h,w = self.h,self.w
        pts = [
            (bx, by, 0),
            (bx, by+h, 0),
            (bx+w*0.8, by+h*0.85, 0),
            (bx+w, by+h*0.5, 0),
            (bx+w*0.8, by+h*0.15, 0),
            (bx, by, 0)
        ]
        self.draw_by_points(pts, (128,0,128), 3)

    def draw_G(self):
        bx,by = self.positions["G"]
        h,w = self.h,self.w
        pts = [
            (bx+w, by+h, 0),
            (bx,   by+h, 0),
            (bx,   by,   0),
            (bx+w, by,   0),
            (bx+w, by+h*0.5, 0),
            (bx+w*0.6, by+h*0.5, 0)
        ]
        self.draw_by_points(pts, (255,165,0), 3)

    def draw_P(self):
        bx,by = self.positions["P"]
        h,w = self.h,self.w
        pts = [
            (bx,   by,   0),
            (bx,   by+h, 0),
            (bx+w, by+h, 0),
            (bx+w, by+h*0.6, 0),
            (bx,   by+h*0.6, 0)
        ]
        self.draw_by_points(pts, (0,0,0), 3)


# --------- MAIN ----------
def main(args=None):
    global settings
    settings = termios.tcgetattr(sys.stdin)

    rclpy.init()
    node = TurtleController()

    try:
        while rclpy.ok():
            key = get_key()

            # flechas funcionando
            if key == '\x1b':
                seq = sys.stdin.read(2)
                if seq == '[A':
                    node.move_relative(0.4, 0)
                elif seq == '[B':
                    node.move_relative(-0.4, 0)
                elif seq == '[C':
                    node.move_relative(0, -0.9)
                elif seq == '[D':
                    node.move_relative(0, 0.9)

            # letras
            k = key.lower()
            if k == 'l': node.draw_L()
            if k == 'n': node.draw_N()
            if k == 'f': node.draw_F()
            if k == 'd': node.draw_D()
            if k == 'g': node.draw_G()
            if k == 'p': node.draw_P()

            if k == 'q':
                break

    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
