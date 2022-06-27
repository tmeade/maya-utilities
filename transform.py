import maya.cmds as cmds

def lerp_rotations(transform_a, transform_b, transform_result):
    axises = ['X','Y','Z']
    colors = ['R','G','B']

    blend_node = cmds.createNode('blendColors', n='{}_blend_rotations_lerp'.format(transform_result))

    for index in range(len(axises)):
        cmds.connectAttr(   '{}.rotate{}'.format(transform_a, axises[index]),
                            '{}.color1{}'.format(blend_node, colors[index]))
        cmds.connectAttr(   '{}.rotate{}'.format(transform_b, axises[index]),
                            '{}.color2{}'.format(blend_node, colors[index]))
        cmds.connectAttr(   '{}.output{}'.format(blend_node, colors[index]),
                            '{}.rotate{}'.format(transform_result, axises[index]))

    return blend_node
