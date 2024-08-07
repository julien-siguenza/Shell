import Sofa
import Sofa.Gui

def main():

    root = Sofa.Core.Node("root")

    createScene(root)

    Sofa.Simulation.init(root)

    Sofa.Gui.GUIManager.Init("myscene", "qglviewer")
    Sofa.Gui.GUIManager.createGUI(root, __file__)
    Sofa.Gui.GUIManager.SetDimension(1080, 1080)
    Sofa.Gui.GUIManager.MainLoop(root)
    Sofa.Gui.GUIManager.closeGUI()

def createScene(rootNode):

    rootNode.addObject('RequiredPlugin', name="Shell")
    rootNode.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
    rootNode.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
    rootNode.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
    rootNode.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Direct")
    rootNode.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
    rootNode.addObject('RequiredPlugin', name="Sofa.Component.Mass")
    rootNode.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
    rootNode.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
    rootNode.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
    rootNode.addObject('RequiredPlugin', name="Sofa.Component.Visual")
    rootNode.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
    rootNode.addObject('RequiredPlugin', name="Sofa.GUI.Component")

    rootNode.gravity = [0, -98.1, 0]
    rootNode.time = 0
    rootNode.animate = 0
    rootNode.addObject('AttachBodyButtonSetting',
        stiffness=0.1,
    )
    rootNode.addObject('DefaultAnimationLoop')

    rootNode.addObject('VisualStyle',
        displayFlags=[
            "hideVisualModels",
            "hideBehaviorModels",
            "showMappings",
            "showForceFields"
        ]
    )

    square = rootNode.addChild('Square')
    square.addObject('EulerImplicitSolver')
    square.addObject('SparseLDLSolver',
        template="CompressedRowSparseMatrixMat3x3d",
    )
    square.addObject('MeshOBJLoader',
        name="loader",
        filename="mesh/square1.obj",
    )
    square.addObject('MeshTopology',
        name="topology",
        src="@loader",
    )
    square.addObject('MechanicalObject',
        template="Rigid3",
    )
    square.addObject('UniformMass',
        totalMass=0.005,
    )
    square.addObject('BoxROI',
        name="box",
        box=[0, 0.9, -0.1, 1, 1, 0.1],
        drawBoxes=True,
    )
    square.addObject('FixedConstraint',
        indices="@box.indices",
    )
    square.addObject('TriangularBendingFEMForceField',
        youngModulus=1.7e3,
        poissonRatio=0.3,
        thickness=0.01,
    )

    visu = square.addChild('Visu')
    visu.addObject('OglModel',
        src="@../topology",
    )
    visu.addObject('IdentityMapping')

if __name__ == '__main__':
    
    main()