import Paciente


class Node:
    def __init__(self, paciente):
        self.paciente = paciente
        self.left = None
        self.right = None

class ColaHospital:
    def __init__(self):
        self.root = None
        self.tamano = 0

    @staticmethod
    def encontrar_padre(root, node):
        if root is None or root == node:
            return None
        queue = [root]
        while queue:
            current = queue.pop(0)
            if current.left == node or current.right == node:
                return current
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return None
    

    def organizar_hacia_arriba(self, node):
        parent = self.encontrar_padre(self.root, node)
        while parent and node.paciente < parent.paciente:
            node.paciente, parent.paciente = parent.paciente, node.paciente
            node = parent
            parent = self.encontrar_padre(self.root, node)


    def insert(self, root, nuevo_nodo):
        queue = [root]
        while queue:
            current = queue.pop(0)
            if not current.left:
                current.left = nuevo_nodo
                self.organizar_hacia_arriba(current.left)
                break
            else:
                queue.append(current.left)
            if not current.right:
                current.right = nuevo_nodo
                self.organizar_hacia_arriba(current.right)
                break
            else:
                queue.append(current.right)


    def registrar_paciente(self, paciente):
        nuevo_nodo = Node(paciente)
        if self.root is None:
            self.root = nuevo_nodo
        else:
            self.insert(self.root, nuevo_nodo)
        self.tamano += 1


    def consultar_proximo_paciente(self):
        return self.root.paciente if self.root else None


    def obtener_ultimo_nodo(self):
        if self.root is None:
            return None
        queue = [self.root]
        ultimo_nodo = None
        while queue:
            ultimo_nodo = queue.pop(0)
            if ultimo_nodo.left:
                queue.append(ultimo_nodo.left)
            if ultimo_nodo.right:
                queue.append(ultimo_nodo.right)
        return ultimo_nodo
    

    def remover_ultimo_nodo(self):
        if self.root is None:
            return
        if self.root.left is None and self.root.right is None:
            self.root = None
            return
        queue = [self.root]
        last_node = None
        parent = None
        while queue:
            last_node = queue.pop(0)
            if last_node.left:
                parent = last_node
                queue.append(last_node.left)
            if last_node.right:
                parent = last_node
                queue.append(last_node.right)
        if parent:
            if parent.right == last_node:
                parent.right = None
            else:
                parent.left = None

    
    @staticmethod
    def organizar_hacia_abajo(node):
        while node.left or node.right:
            nodo_mas_pequeño = node
            if node.left and node.left.paciente < nodo_mas_pequeño.paciente:
                nodo_mas_pequeño = node.left
            if node.right and node.right.paciente < nodo_mas_pequeño.paciente:
                nodo_mas_pequeño = node.right
            if nodo_mas_pequeño == node:
                break
            node.paciente, nodo_mas_pequeño.paciente = nodo_mas_pequeño.paciente, node.paciente
            node = nodo_mas_pequeño


    def atender_siguiente(self):
        if self.root is None:
            return None
        next_patient = self.root.paciente
        if self.tamano == 1:
            self.root = None
        else:
            ultimo_nodo = self.obtener_ultimo_nodo()
            if ultimo_nodo:
                self.root.paciente = ultimo_nodo.paciente
                self.remover_ultimo_nodo()
                self.organizar_hacia_abajo(self.root)
        self.tamano -= 1
        return next_patient


    def consultar_pacientes_en_espera(self):
        return self.obtener_todos_los_pacientes(self.root)

    @staticmethod
    def obtener_todos_los_pacientes(root):
        if root is None:
            return []
        queue = [root]
        pacientes = []
        while queue:
            current = queue.pop(0)
            pacientes.append(current.paciente)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return pacientes


    def consultar_pacientes_por_triaje(self, triaje):
        return [p for p in self.consultar_pacientes_en_espera() if p.triaje == triaje]


    @staticmethod
    def encontrar_nodo(root, parent, paciente_id):
        if root is None:
            return None, None
        queue = [(root, parent)]
        while queue:
            current, current_parent = queue.pop(0)
            if current.paciente.id == paciente_id:
                return current, current_parent
            if current.left:
                queue.append((current.left, current))
            if current.right:
                queue.append((current.right, current))
        return None, None
    

    def eliminar_paciente(self, paciente_id):
        node, parent = self.encontrar_nodo(self.root, None, paciente_id)
        if node:
            if self.tamano == 1:
                self.root = None
            else:
                last_node = self.obtener_ultimo_nodo()
                if last_node:
                    node.paciente = last_node.paciente
                    self.remover_ultimo_nodo()
                    self.organizar_hacia_abajo(node)
            self.tamano -= 1

    
    def printT(self, node, prefix="", is_left=True):
        if not node:
            print("Empty Tree")
            return
        if node.right:
            self.printT(node.right, prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + str(node.paciente.nombre))
        if node.left:
            self.printT(node.left, prefix + ("    " if is_left else "│   "), True)
