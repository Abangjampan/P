-                  1
1607227761
1
__data
require "cocos.cocos2d.Cocos2d"
require "cocos.cocos2d.Cocos2dConstants"
require "cocos.cocos2d.functions"

__G__TRACKBACK__ = function(msg)
    local msg = debug.traceback(msg, 3)
    print(msg)
    return msg
end

-- opengl
require "cocos.cocos2d.Opengl"
require "cocos.cocos2d.OpenglConstants"
-- audio
require "cocos.cocosdenshion.AudioEngine"
-- cocosstudio
if nil ~= ccs then
    require "cocos.cocostudio.CocoStudio"
end
-- ui
if nil ~= ccui then
    require "cocos.ui.GuiConstants"
    require "cocos.ui.experimentalUIConstants"
end

-- extensions
require "cocos.extension.ExtensionConstants"
-- network
require "cocos.network.NetworkConstants"
-- Spine
if nil ~= sp then
    require "cocos.spine.SpineConstants"
end

require "cocos.cocos2d.deprecated"
require "cocos.cocos2d.DrawPrimitives"

-- Lua extensions
require "cocos.cocos2d.bitExtend"

-- CCLuaEngine
require "cocos.cocos2d.DeprecatedCocos2dClass"
require "cocos.cocos2d.DeprecatedCocos2dEnum"
require "cocos.cocos2d.DeprecatedCocos2dFunc"
require "cocos.cocos2d.DeprecatedOpenglEnum"

-- register_cocostudio_module
if nil ~= ccs then
    require "cocos.cocostudio.DeprecatedCocoStudioClass"
    require "cocos.cocostudio.DeprecatedCocoStudioFunc"
end


-- register_cocosbuilder_module
require "cocos.cocosbuilder.DeprecatedCocosBuilderClass"

-- register_cocosdenshion_module
require "cocos.cocosdenshion.DeprecatedCocosDenshionClass"
require "cocos.cocosdenshion.DeprecatedCocosDenshionFunc"

-- register_extension_module
require "cocos.extension.DeprecatedExtensionClass"
require "cocos.extension.DeprecatedExtensionEnum"
require "cocos.extension.DeprecatedExtensionFunc"

-- register_network_module
require "cocos.network.DeprecatedNetworkClass"
require "cocos.network.DeprecatedNetworkEnum"
require "cocos.network.DeprecatedNetworkFunc"

-- register_ui_moudle
if nil ~= ccui then
    require "cocos.ui.DeprecatedUIEnum"
    require "cocos.ui.DeprecatedUIFunc"
end

-- cocosbuilder
require "cocos.cocosbuilder.CCBReaderLoad"

-- physics3d
require "cocos.physics3d.physics3d-constants"

if CC_USE_FRAMEWORK then
    require "cocos.framework.init"
end
UnityFS    5.x.x 2017.4.21f1       
�   A   [   C  �  �  
&     � CAB-f63f6d0523eeb799c12da0965edfb7ee �  ]  �     �    2017.4.21f1 
      s ���-��o���1��ո��U�$   �       �7  �����. � �    H �� P  s1  �10  @ � �  � �T    �Q  �j  �p  0    �  S     s � �*@  3  < 	 E 
 N  W  ` 
 i  r  {  �  �  �  �  �  � � �N0��  �  �  ` �` ` ` ` ` �` `  ` !` "` SL  ��8# �m_ExecutionOrder Hash128 m_Properties � bytes[0]	 1	 2	 3	 4	 5	 6	 7	 8	 9Q [ \ 1] 1^ 1_ �15] m_ClassName m_ @spac �Assembly �IsEditorScript r  �bu���y$CBb��<����q���KIɴ�������4 �v �( A�? S. �	 �']�A Sh ��`  � `   �`  
//	/
//S� ��� 	` 
 
`   [ ` � � � � �  � ,� � �  6� � � � F� � �  K� � � � ]� � �   h� !� "� #� v� $� %� & ~� '� (� ) �m_FileID�athID textures PPtr<$T �2D> material M T> fbx �GameObject> animar  dshader S 2> "	��rdh4��&��)�SO/� � S S�"	A"	ASS ` $ ��� H $�  k-��S� �60 �
�		� 
� 
���S� �>�
x  *D"	 *�Component 
 ePair c 7�m_Layer m_Tag��Active �����_F��ZWȴ-OBIr�:   �~  �
a 66v � `  �"y` ��t 	�$, 
"� 6 � �  
� q�  0 0 P�  ` P` 8P 0 9� 0 �Uq&C P�  P\� PqPP � bt Q�  �  � �0 q� �  �n0 ��� �!�"�#��q�q�q&HX'X	H (� H )� � *�  �� +x��8,8  � -  H�� .� /H0H1H2H3H4H5H ` "
H 6` 7` 8` 9��ssetBundle��eloadTable��Container9 bInfo p5 TIndex
 `Size a# � m_MainA pRuntimeI�atibility�� ��Dependencies@�StreamedScene� �ExplicitDataLayout� @Flag> 4  �
Bes ��v�xIB��7��4U�[/t�KD� �!� !  0 W�  �"y W  �� (W x ��x 
x x ` : 
` ` ` `  �G��	�	�	Ρ�	* *� H R� ���;	 qocalRot-� x y z w APosi  1ScapChildre aFatherC�c����^��� ]��K\�e�,"�$|� �����y����|	#    b  ����d����  D@	 l /  �archive:/cab-f2f459222c9238e5954e6e42f2874ba6% 
c  �BBase? �$  �:�-CSharp-firstpass.dlld ,� �  p=�$��� �=et	�כ� ��_�U7m� ����.ވ� ��͠{y� �gI�\E|�� � ��G�OutBattl�   p�1s/sI3ing �art/android/hero�
d= �.unity3d	� � � � � 4� \� 0� �prefabs/outb� �  T � \ -PD ��variantsA �  
� .�? +�? P     