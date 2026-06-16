# BlackHole Engine SDK Upgrade Notes

Source API: https://developer.bjblackhole.com/api/developercenter/Doc/DocItem/list/bydcid?dcid=3a0b9cac-880a-697b-9bf4-6328c4b94612

This file is generated from the official update-note API. Use it for SDK upgrade, compatibility, bug-fix, and migration notes. The API Markdown reference is maintained as latest-only because BlackHole Engine APIs are expected to be backward-compatible.

When a user reports an SDK error, upgrade regression, changed behavior, missing API, runtime exception, initialization problem, or version-specific bug, search this file before answering.

## Current Latest

- SDK: `SDK_V3.2.0.3772`
- Release date: `2026-06-12`
- API reference: `blackhole-engine-api.SDK_V3.2.0.3772.md`

## Upgrade Notes

### SDK_V3.2.0.3772 - 2026-06-12

- Title: WebSDK 更新时间：2026.06.12
- SDK package: `Sources/2026_06_12_14_57_57_3a21cccc-5f16-964d-f88a-29cd4eb1aa43_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine SDK_v3.2.0.3772.zip`
- API manual: `Sources/2026_06_12_14_57_53_3a21cccc-50c1-3efa-cb0d-59f9e8dc6800_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine API_Web-v3.2.0.3772.docx`

1.投射（Projection）新增接口：setShpSelClr、getShpSelClr
2.修复了设置体剖切数据异常报错的问题

### SDK_V3.2.0.3767 - 2026-06-02

- Title: WebSDK 更新时间：2026.06.02
- SDK package: `Sources/2026_06_02_17_20_46_3a2199cf-8734-678e-19d0-a5a5b647170b_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine SDK_v3.2.0.3767.zip`
- API manual: `Sources/2026_06_02_17_20_41_3a2199cf-74eb-7161-69a6-f0f33f968ea0_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine API_Web-v3.2.0.3767.docx`

1.投射（Projection）新增接口：setTexClrMult、getTexClrMult
2.BIM（BIM）新增接口：getDateSetElemIds
3.修复了矢量无法编辑的异常
4.优化了球面效果下地面相机的有效经纬度范围

### SDK_V3.2.0.3757 - 2026-04-17

- Title: WebSDK 更新时间：2026.04.17
- SDK package: `Sources/2026_05_25_17_51_56_3a2170b9-315a-21e6-1816-cc4bc8fccdca_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine SDK_v3.2.0.3757.zip`
- API manual: `Sources/2026_05_25_17_51_53_3a2170b9-2333-0e04-04aa-8656fff78c5c_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine API_Web-v3.2.0.3757.docx`

1.公共模块（Common）新增接口：setLogDepthEnable、getLogDepthEnable
2.相机（Camera）接口：Camera.getCamLocate新增参数：camUpDir、camRightDir
3.地形（Terrain）新增接口：refreshDataSet
4.引擎模块新增接口：setURLGolExtProxy、delURLGolExtProxy
5.修复了地形区域变换时范围分析错误的问题
6.修复了使用相机朝向信息定位时，z值趋近于1的数据效果异常问题
7.新增模块投射（Projection）
8.投射（Projection）新增接口：setData、getData、delData、getAllProjectionId、setDefaultInfo、getDefaultInfo、startEditState、endEditState、startAddProjectionState、endAddProjectionState、getCurProjectionId、setClipPlaneEditType、getClipPlaneEditType、setPitch、resetClipPlane、setShowState、getIdsByShowState、setVisible、getProjectionIdByVisible、setClipPlaneValid、getClipPlaneValid、setTexPath、getTexPath、setType、getType、setPerspParam、getPerspParam、setOrthoParam、getOrthoParam、setCamPos、getCamPos、setTargetPos、getTargetPos、setNearFarPlaneOffset、getNearFarPlaneOffset、setUVRect、getUVRect、setUVMap、getUVMap、setShpClr、getShpClr、setProjShpCanOverlap、getProjShpCanOverlap、setProjectionMask
9.新增监听事件：REEditProjFinish、REAddProjFinish、REProjPosChange

### SDK_V3.2.0.3690 - 2026-04-17

- Title: WebSDK 更新时间：2026.04.17
- SDK package: `Sources/2026_04_17_18_29_21_3a20ad29-c9a4-31b7-bb7b-f2cdc01a50f9_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine SDK_v3.2.0.3690.zip`
- API manual: `Sources/2026_04_17_18_29_14_3a20ad29-b043-7df3-1ebe-d5689576aad7_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine API_Web-v3.2.0.3690.docx`

1.优化了场景加载CAD矢量的相机效果
2.修复了Math.getPtListTran计算角度旋转时法线不正确的异常

### SDK_V3.2.0.3669 - 2026-04-03

- Title: WebSDK 更新时间：2026.04.03
- SDK package: `Sources/2026_04_10_15_56_54_3a208891-b419-91cc-27e0-d3db0ee5bd81_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine SDK_v3.2.0.3669.zip`
- API manual: `Sources/2026_04_03_10_59_15_3a206374-af91-48bd-23c1-1e9e1b8cfcff_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine API_Web-v3.2.0.3669.docx`

1.单构件（Entity）新增接口：setShadowPrefer
2.修复了水面颜色不透明度参数设置异常的问题
3.修复了贴底测量功能在大坐标下测量不准确的问题
4.优化了CAD一系列特殊类型和属性，如文字、线条、填充等效果
5.360全景（Panorama）新增接口：setCamLocateToRotate
6.监听事件新增：REPanLocateCam
7.修复了相机定位小构件后看不到构件的问题
8.优化了地形影响和矢量一起加载时总包围盒的计算方式
9.修复了多项目单构件批量选择位置编辑，显示效果和实际操作不准确的问题
10.修复了单体化后绑定已经偏移的项目，定位出现异常的问题
11.CAD（CAD）新增接口：getLayoutLodRange、setCurShowLodRange、getCurShowLodRange
12.数学计算（Math）新增接口：getVectorCross、getDirection、getPtListTran

### SDK_V3.2.0.3624 - 2026-03-05

- Title: WebSDK 更新时间：2026.03.05
- SDK package: `Sources/2026_03_09_16_51_02_3a1fe3f7-c2f6-5090-d134-39d297406d71_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine SDK_v3.2.0.3624.zip`
- API manual: `Sources/2026_03_09_16_50_57_3a1fe3f7-b128-56e9-b566-c2a7b52d19bc_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine API_Web-v3.2.0.3624.docx`

**为提升系统稳定性与使用体验，现已对水面、拍平、挖洞、挖坑相关功能完成优化重构，原低版本接口已正式废弃。请相关用户尽快调整业务代码，切换使用新版接口，避免因接口废弃影响功能正常使用。**
1.**新增模块**：矢量编辑（ShpEdit）、新增单体化（Monomer）、新挤出（Extrude）
2.**矢量编辑（ShpEdit）新增接口**：setData、getData、getAllShpId、delData、startShpEditState、endShpEditState、startAddShpState、endAddShpState、getCurShpId、startClipShpState、endClipShpState、setVisible、getVisible、setShpClr、getShpClr、setShpClipClrPool、getShpClipClrPool、delShpClipClrPool、setCamToData
3.**单体化（Monomer）新增接口**：setData、getData、delData、getAllMonomerId、setVisible、getVisible、startEditState、endEditState、startAddMonomerState、endAddMonomerState、getCurMonomerId、setEditApplyDataSetId、getEditApplyDataSetId、setDefaultClr、getDefaultClr、setClr、getClr、setDefaultEditMinMaxHeight、getDefaultEditMinMaxHeight、setEditAutoCalcMinMaxHeight、getEditAutoCalcMinMaxHeight、setMinMaxHeight、getMinMaxHeight、setExpandDist、getExpandDist、addToSel、delFromSel、getAllCurSel、setSelAttr、getSelAttr、setMultiSel、getMultiSel、setCanProbe、getCanProbe、setHighlightAttr、getHighlightAttr、setCamToData、getErrorDrawMonomerIds
4.**矢量编辑（ShpEdit）新增接口**：setData、getData、delData、getCurExtrudeId、getAllExtrudeId、setDataSetScope、getDataSetScope、addExtrudeFaceTex、delAllExtrudeFaceTex、startEditState、endEditState、startAddExtrudeState、endAddExtrudeState、setExtrudeTexId、getExtrudeTexId、setDepthLimitRange、getDepthLimitRange、setShowType、getShowType、setVisible、getVisible、setCamToData、getErrorDrawExtrudeIds、setShowState、getIdsByShowState
5.**监听事件新增回调**：REAddWaterRgnCheck、REAddWaterRgnFinish、REEditExtrudeFinish、REAddExtrudeRgnCheck、REAddExtrudeRgnFinish、REEditMonomerFinish、REAddMonomerRgnCheck、REAddMonomerRgnFinish、REEditShpFinish、REAddShpRgnCheck、REAddShpRgnFinish、REShpAddClipFace、REShpClipFinish
6.**水面（Water）模块重构，并新增接口**：setData、getCurWaterName、getAllWaterName、startEditState、endEditState、startAddWaterState、endAddWaterState、setVisible、getVisible、setClr、getClr、setBlendDist、getBlendDist、setDefaultAttr、getErrorDrawWaterIds、getExpandDist、setExpandDist、getDepthBias、setDepthBias、getVisDist、setVisDist、setShowState、getIdsByShowState
7.修复了点云选中消失的异常

**水面（Water）模块重构**
| 功能 | v-old | v-new | 差异说明 |
|-----|------|------|---------|
| 创建水域对象 | Water.loadData | Water.setData | 调整区域顶点对象名称及结构，一维数组结构转变为二维数组结构，增加多区域功能 |
| 获取水域对象 | Water.getData | Water.getData | 入参调整为集合结构，返回对象字段调整 |
| 通过水面名称删除指定的水面对象 | Water.delData | Water.delData | 入参调整为集合结构 |
| 把当前场景中所有水面对象全部删除 | Water.delAllData | — | 方法移除，功能合并到 Water.delData 中 |
| 根据水面名称定位到水面 | Water.setCamToData | Water.setCamToData | 入参调整为集合结构 |

**挖洞（Excavate）模块移除功能变更为挤出（Extrude）模块**
| 功能 | v-old | v-new | 差异说明 |
|-----|------|------|---------|
| 添加挖洞面上使用的纹理 | Excavate.addExcavateFaceTex | Extrude.addExtrudeFaceTex | 接口名称调整 |
| 清除挖洞面使用的纹理 | Excavate.clearAllExcavateFaceTex | Extrude.addExtrudeFaceTex | 接口名称调整 |
| 创建一个挖洞区域对象 | Excavate.createExcavateObj | Extrude.setData | 调整区域顶点对象名称及结构，一维数组结构转变为二维数组结构，增加了多区域功能，入参对象结构和参数名称调整 |
| 根据标识删除一个挤出区域对象 | Excavate.delExcavateObj | Extrude.delData | 入参调整为集合结构 |
| 设置挖洞对象的类型 | Excavate.setExcavateType | Extrude.setShowType | 接口名称调整 |
| 获取挖洞对象的类型 | Excavate.getExcavateType | Extrude.getShowType | 接口名称调整 |
| 设置挖洞效果是否允许覆盖生效 | Excavate.setExcavateEffect | Extrude.setDataSetScope | 接口名称调整 |
| 获取挖洞效果是否允许覆盖生效 | Excavate.getExcavateEffect | Extrude.getDataSetScope | 接口名称调整 |
| 聚焦到指定的挖洞对象区域 | Excavate.locateToExcavateObj | Extrude.setCamToData | 入参调整为集合结构 |

**瓦片（Grid）模块移除倾斜摄影拍平，功能变更为挤出（Extrude）模块**
| 功能 | v-old | v-new | 差异说明 |
|-----|------|------|---------|
| 根据项目名称设置局部拍平区域 | Grid.setDataSetFlatRegion | Extrude.setData | 调整区域顶点对象名称及结构，一维数组结构转变为二维数组结构，增加了多区域功能，入参对象结构和参数名称调整，局部拍平需要传递数据集标识 |
| 设置当前场景下的全局拍平区域 | Grid.setDataSetFlatRegion | Extrude.setData | 调整区域顶点对象名称及结构，一维数组结构转变为二维数组结构，增加了多区域功能，入参对象结构和参数名称调整，全局拍平不需要传递数据集标识 |
| 清除一组拍平区域 | Grid.removeFlatRegion | Extrude.delData | 接口名称调整 |
| 重置一组拍平区域 | Grid.resetFlatRegion | ---- | 移除，功能合并到Extrude.delData中 |
| 设置通过setFlatGolRegion接口设置的拍平数据是否有效 | Grid.setFlatRegionEffective | ---- | 移除，功能合并到Extrude.setVisible 中 |
| 获取通过setFlatGolRegion接口设置的拍平数据是否有效 | Grid.getFlatRegionEffective | ---- | 移除，功能合并到Extrude.setVisible 中 |
| 清空setDataSetFlatRegion 接口设置的局部拍平区域 | Grid.setFlatRegionEffective | ---- | 移除，功能合并到Extrude.getVisible中 |
| 设置通过setDataSetFlatRegion 接口设置的拍平数据是否有效 | Grid.getLocalFlatRegionEffective | ---- | 移除，功能合并到Extrude.setVisible 中 |
| 获取通过setDataSetFlatRegion 接口设置的拍平数据是否有效 | Grid.getLocalFlatRegionEffective | ---- | 移除，功能合并到Extrude.getVisible中 |

**瓦片（Grid）模块移除倾斜摄影单体化，功能变更为单体化（Monomer）模块**
| 功能 | v-old | v-new | 差异说明 |
|-----|------|------|---------|
| 预加载倾斜摄影单体化数据 | Grid.setMonomerElemData | Monomer.setData | 调整区域顶点对象名称及结构，一维数组结构转变为二维数组结构，增加了多区域功能，入参对象结构和参数名称调整 |
| 添加单体化区域到选择集中 | Grid.addToSelMonomerElemIDs | Monomer.addToSel | 接口名称调整 |
| 将单体化区域从选择集中移除 | Grid.removeFromSelMonomerElemIDs | Monomer.delFromSel | 接口名称调整 |
| 获取当前单体化选择集的ID集合 | Grid.getSelMonomerElemIDs | Monomer.getAllCurSel | 接口名称调整 |
| 设置单体化选择集的颜色和透明度 | Grid.setSelMonomerElemClr | Monomer.setSelAttr | 入参对象结构和参数名称调整 |
| 设置单体化区域隐藏状态下的颜色 | Grid.setMonomerElemHideClr | Monomer.setDefaultClr | 接口名称调整 |
| 设置单体化矢量是否可以被选中 | Grid.setMonomerElemSelEnable | Monomer.setCanProbe | 接口名称调整 |
| 设置单体化矢量显示和隐藏 | Grid.setMonomerElemVisible | Monomer.setVisible | 接口名称调整 |
| 删除单体化矢量 | Grid.delMonomerElem | Monomer.delData | 接口名称调整 |

### SDK_V3.2.0.3587 - 2026-01-30

- Title: WebSDK 更新时间：2026.01.30
- SDK package: `Sources/2026_01_30_15_50_36_3a1f200e-c809-fadd-7566-e8fa97ef2b0a_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine SDK_v3.2.0.3587.zip`
- API manual: `Sources/2026_01_30_15_50_32_3a1f200e-b67e-4481-f5f6-6ebf0a858b2a_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine API_Web-v3.2.0.3587.docx`

1. 新增监听事件：RESystemKeyDown、RESystemSel
2. 鼠标探测（Probe）新增接口：getCurSelInfo
3. 优化了设置剖切数据效果，受相机方位影响的问题

### SDK_V3.2.0.3559 - 2026-01-09

- Title: WebSDK 更新时间：2026.01.09
- SDK package: `Sources/2026_01_09_16_42_38_3a1eb418-dcd6-c449-4697-3185fe76fcec_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine SDK_v3.2.0.3559.zip`
- API manual: `Sources/2026_01_09_16_42_33_3a1eb418-cab6-5a61-2a86-864629a09b09_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine API_Web-v3.2.0.3559.docx`

1. 小地图（MiniMap）新增接口：setCurViewportRange
2. 新增监听事件：RECADSwitchLayoutFinished

### SDK_V3.2.0.3547 - 2025-12-29

- Title: WebSDK 更新时间：2025.12.29
- SDK package: `Sources/2025_12_29_14_40_18_3a1e7b02-e8d3-1a15-8a6c-1d801a44e608_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine SDK_v3.2.0.3547.zip`
- API manual: `Sources/2025_12_29_14_40_13_3a1e7b02-d4fd-a0fb-1e0c-7a0159592b52_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine API_Web-v3.2.0.3547.docx`

1. 地形（Terrain）新增接口：setGolTerrShpAncTextVisLodRange、getGolTerrShpAncTextVisLodRange、setGolTerrShpLineTextVisLodRange、getGolTerrShpLineTextVisLodRange
2. 几何图形（Geometry）调整接口：addPolylineShp增加字段，实现投影贴地材质纹理效果

### SDK_V3.2.0.3528 - 2025-12-16

- Title: WebSDK 更新时间：2025.12.16
- SDK package: `Sources/2025_12_16_11_22_03_3a1e375a-bbd1-1196-5883-4574ab5e082a_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine SDK_v3.2.0.3528.zip`
- API manual: `Sources/2025_12_16_11_21_58_3a1e375a-aa0b-5603-8b25-26996164b25a_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine API_Web-v3.2.0.3528.docx`

1. 修复了选中标记闪烁的问题
2. 修复了部分模型资源刷新相关的问题
3. 调整了接口：Edit.startEdit的返回值
4. 引擎模块新增接口：getCurInteractState
5. 几何图形（Geometry）新增接口：setCustomShpPresetVisDist

### SDK_V3.2.0.3516 - 2025-12-05

- Title: WebSDK 更新时间：2025.12.05
- SDK package: `Sources/2025_12_05_18_00_21_3a1e0021-712b-5d39-21cb-965507abf784_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine SDK_v3.2.0.3516.zip`
- API manual: `Sources/2025_12_05_18_00_14_3a1e0021-53f8-24e3-0053-e42fe46d9a19_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine API_Web-v3.2.0.3516.docx`

1. 公共模块（Common）新增接口：setShpOITLev、getShpOITLev
2. 公共模块（Common）调整接口：setSceOITLev、getSceOITLev的参数使用
3. 修复了地形矢量锚点添加显示异常的问题
4. 修复了地形影像坐标变换的缓存信息数组过小的问题
5. 数学计算（Math）新增接口：getAABBSpatialRelation、getAABBToPtListRelation、getPtListSpatialRelation、getPtListAABB、isPtInTriangle、isPtInPolygonCylindricalRegion、getPtToPolyEdgeShortestIntersect
6. 修复了含有坐标系的非常规模型，定位构件，位置偏移异常的问题
7. 增加了选中标记的效果
8. BIM（BIM）新增接口：setSelMarkClr、getSelMarkClr

### SDK_V3.2.0.3487 - 2025-11-24

- Title: WebSDK 更新时间：2025.11.24
- SDK package: `Sources/2025_11_24_09_49_37_3a1dc5ba-3628-7c59-9872-7383daa24c87_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine SDK_v3.2.0.3487.zip`
- API manual: `Sources/2025_11_24_09_49_34_3a1dc5ba-2859-10e5-6fb4-8aae7fb8d059_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine API_Web-v3.2.0.3487.docx`

1. 新增模块数学计算（Math）
2. 数学计算（Math）新增接口：getLineInfo、getCustomFaceExpand、getCustomFaceExpand
3. 相机（Camera）新增接口：setCamLocateToBoundByDir
4. CAD（CAD）新增接口：getElemBV、setBimCadMapPoints、getBimToCadCamDir、getBimToCadPoint、getCadToBimPoint、getCadToBimBV、getBimToCadBV
5. 修复了删除单构件导致内存崩溃的异常
6. 优化了自定义矢量线构面检测的效果

### SDK_V3.2.0.3468 - 2025-11-18

- Title: WebSDK 更新时间：2025.11.18
- SDK package: `Sources/2025_11_18_10_04_51_3a1da6e1-fe8e-93c7-f177-f54363edd006_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine SDK_v3.2.0.3468.zip`
- API manual: `Sources/2025_11_18_10_04_46_3a1da6e1-ed9e-1480-01fb-85b016bc91d3_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine API_Web-v3.2.0.3468.docx`

1. 公共模块（Common）新增接口：setMaxTexGroupAtlasSize、getMaxTexGroupAtlasSize
2. 锚点（Anchor）新增接口：setCustomMaxTexSize、getCustomMaxTexSize
3. 修复了在添加世界坐标系的条件下测量数据异常的问题
4. BIM（BIM）新增接口：setDiffCoef
5. 瓦片（Grid）新增接口：setDiffCoef

### SDK_V3.2.0.3463 - 2025-11-11

- Title: WebSDK 更新时间：2025.11.11
- SDK package: `Sources/2025_11_11_10_05_26_3a1d82d6-0380-ea0b-adfc-1ff0096d0bcb_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine SDK_v3.2.0.3463.zip`
- API manual: `Sources/2025_11_11_10_05_18_3a1d82d5-e5b5-a76a-ba61-8f8ef1792e16_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine API_Web-v3.2.0.3463.docx`

1. 优化了地形矢量数据不同角度查看的效果
2. 优化了WMS数据的渲染效果

### SDK_V3.2.0.3453 - 2025-11-03

- Title: WebSDK 更新时间：2025.11.03
- SDK package: `Sources/2025_11_03_15_14_42_3a1d5abe-4879-a4c7-2ce6-192fc09e9910_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine SDK_v3.2.0.3453.zip`
- API manual: `Sources/2025_11_03_15_14_38_3a1d5abe-389f-bdae-f119-c989c99f8a96_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine API_Web-v3.2.0.3453.docx`

1. 相机（Camera）新增接口：setCamAlignTerrainPage、getCamAlignTerrainPage
2. 优化了相机在地形影像上的操作效果
3. 优化了CAD文字显示效果
4. 修复了某些数据集卸载后造成渲染出现白色背景的异常问题

### SDK_V3.2.0.3433 - 2025-10-29

- Title: WebSDK 更新时间：2025.10.29
- SDK package: `Sources/2025_10_29_15_33_57_3a1d4110-1b5e-e25d-7c0e-3ff48a3cea0b_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine SDK_v3.2.0.3433.zip`
- API manual: `Sources/2025_10_29_15_33_54_3a1d4110-0edf-3cad-c3de-3c8343240de8_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine API_Web-v3.2.0.3433.docx`

1. 坐标（Coordinate）新增接口：getTransCoords
2. 优化了车流模拟的渲染效果

### SDK_V3.2.0.3427 - 2025-10-15

- Title: WebSDK 更新时间：2025.10.15
- SDK package: `Sources/2025_10_28_10_01_39_3a1d3ab9-842c-f44c-f010-a2c282faffc2_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine SDK_v3.2.0.3427.zip`
- API manual: `Sources/2025_10_28_10_01_33_3a1d3ab9-6e78-455a-4dbe-6940befc14e9_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine API_Web-v3.2.0.3427.docx`

1. 几何图形（Geometry）新增接口：setCamToShpList、setShpVisible、getShpVisible
2. 地形（Terrain）新增接口：setUnitLayerClr、getUnitLayerClr、addTerrShpAnc、getAllTerrShpAnc、delTerrShpAnc、setCamToAnc、setTerrShpAncVisible、getTerrShpAncVisible、addTerrShpLine、delTerrShpLine、setCamToTerrShpLine、setTerrShpLineVisible、getTerrShpLineVisible
3. 优化了地形数据相机缩放效果

### SDK_V3.2.0.3396 - 2025-10-15

- Title: WebSDK 更新时间：2025.10.15
- SDK package: `Sources/2025_10_15_18_01_30_3a1cf97e-2991-b0ae-8d87-a27c1e338e78_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine SDK_v3.2.0.3396.zip`
- API manual: `Sources/2025_10_15_18_01_26_3a1cf97e-1bc9-e7f7-1e6f-040cca11992c_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine API_Web-v3.2.0.3396.docx`

1. 地形（Terrain）新增接口：setUnitMinVirPxlH、getUnitMinVirPxlH、setTerrProjectMode、getTerrProjectMode

### SDK_V3.2.0.3388 - 2025-10-11

- Title: WebSDK 更新时间：2025.10.11
- SDK package: `Sources/2025_10_11_17_49_06_3a1ce4d9-6014-f72c-9011-c6205c23035d_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine SDK_v3.2.0.3388.zip`
- API manual: `Sources/2025_10_11_17_49_01_3a1ce4d9-4bf4-ec13-3fc8-a4ad613f3728_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine API_Web-v3.2.0.3388.docx`

1. 瓦片（Grid）新增接口：getValidState
2. 公共模块（Common）新增接口：setShpCoverDottedEnable、getShpCoverDottedEnable

### SDK_V3.2.0.3384 - 2025-09-30

- Title: WebSDK 更新时间：2025.09.30
- SDK package: `Sources/2025_09_30_17_34_08_3a1cac25-b99a-80e4-ed36-143028b23119_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine SDK_v3.2.0.3384.zip`
- API manual: `Sources/2025_09_30_17_34_00_3a1cac25-9981-1cf9-e8e4-2da91e80477d_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine API_Web-v3.2.0.3384.docx`

1.修复了UI面板剖切按钮的状态和接口调用不匹配的异常问题

### SDK_V3.2.0.3379 - 2025-09-25

- Title: Web SDK 更新时间：2025.09.25
- SDK package: `Sources/2025_09_26_10_22_28_3a1c9601-15ee-6302-5bb3-8469c741344b_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine SDK_v3.2.0.3379.zip`
- API manual: `Sources/2025_09_25_19_28_41_3a1c92ce-cac6-d63d-08a4-6ea089953c18_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine API_Web-v3.2.0.3379.docx`

1. 剖切（Clip）新增接口：setClipBoxHoverClrInfo、getClipBoxHoverClrInfo

### SDK_V3.2.0.3376 - 2025-09-25

- Title: Web SDK 更新时间：2025.09.25
- SDK package: `Sources/2025_09_25_15_41_33_3a1c91fe-d986-f58e-7bf0-43d36eb25969_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine SDK_v3.2.0.3376.zip`
- API manual: `Sources/2025_09_25_15_41_29_3a1c91fe-cc0a-2f4c-ce62-270808af6693_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine API_Web-v3.2.0.3376.docx`

1. 图形显示（Graphics）新增接口：setLocalLanguage、getLocalLanguage，实现中英语言切换

### SDK_V3.2.0.3362 - 2025-09-19

- Title: Web SDK 更新时间：2025.09.19
- SDK package: `Sources/2025_09_19_16_54_01_3a1c735b-0972-eff8-63ff-db3c49a7746c_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine SDK_v3.2.0.3362.zip`
- API manual: `Sources/2025_09_19_14_23_07_3a1c72d0-e2a9-133a-4de7-bcd7d9bb0b04_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine API_Web-v3.2.0.3362.docx`

1. 优化了锚点、标签元素被不透明物体遮挡情况下的显示效果
2. 监听事件调整：RECADSelElement 事件增加点击空白区域回调
3. 监听事件新增：RECADCommentDrawFinish，实现CAD添加标注完成事件回调

### SDK_V3.2.0.3334 - 2025-09-09

- Title: Web SDK 更新时间：2025.09.09
- SDK package: `Sources/2025_09_09_14_21_15_3a1c3f4f-9493-c285-a532-386e287f7d59_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine SDK_v3.2.0.3334.zip`
- API manual: `Sources/2025_09_09_14_21_06_3a1c3f4f-73bc-ccc6-048a-81ed5888d4cb_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine API_Web-v3.2.0.3334.docx`

1. 修复了单构件路径动画失败的异常问题

### SDK_V3.2.0.3323 - 2025-09-04

- Title: Web SDK 更新时间：2025.09.04
- SDK package: `Sources/2025_09_04_18_57_38_3a1c268c-d37c-b287-3cf3-ca6f10d9b6ee_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine SDK_v3.2.0.3323.zip`
- API manual: `Sources/2025_09_04_19_06_00_3a1c2694-79fd-a803-580f-1f881cd331af_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine API_Web-v3.2.0.3323.docx`

1. 锚点（Anchor）接口：addAnc新增字段，实现锚点文字背景圆角和边距效果
2. 几何图形（Geometry）接口：addPolyFenceShp新增字段，实现自定义纹理效果
3. 动画（Animation）接口：addAnimAreaBuffer新增字段，实现投影到地形和倾斜摄影效果
4. 测量（Measure）接口：addGroupData调整调用模式，允许在非测量模式下绘制自定义测量矢量
5. 优化了拾取点精度问题
6. 优化了获取地形不透明度数值异常的问题

### SDK_V3.2.0.3303 - 2025-08-27

- Title: Web SDK 更新时间：2025.08.27
- SDK package: `Sources/2025_08_28_17_53_21_3a1c0245-7521-9640-9f04-45294cf81540_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine SDK_v3.2.0.3303.zip`
- API manual: `Sources/2025_08_28_17_53_16_3a1c0245-60ae-e4e2-41ac-9de08b5a2f88_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine API_Web-v3.2.0.3303.docx`

1. 修复了单构件路径动画播放过程单构件消失的问题
2. 修复了单构件路径动画播放过程单构件抖动旋转的问题
3. 优化了CAD部分文字显示异常的问题

### SDK_V3.2.0.3292 - 2025-08-21

- Title: Web SDK 更新时间：2025.08.21
- SDK package: `Sources/2025_08_21_17_28_57_3a1bde22-9b23-bf0c-b4c5-f17474c13221_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine SDK_v3.2.0.3292.zip`
- API manual: `Sources/2025_08_21_17_28_53_3a1bde22-88cc-789c-abcf-536b93c3cf39_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine API_Web-v3.2.0.3292.docx`

1. CAD增加用户坐标系支持

### SDK_V3.2.0.3287 - 2025-08-13

- Title: Web SDK 更新时间：2025.08.13
- SDK package: `Sources/2025_08_14_15_22_27_3a1bb9a2-4411-1727-00c4-bf5142f21735_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine SDK_v3.2.0.3287.zip`
- API manual: `Sources/2025_08_13_19_17_57_3a1bb553-82c8-fe13-bdbd-585500efea36_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine API_Web-v3.2.0.3287.docx`

1. 优化第三人称漫游功能
2. 相机（Camera）移除接口：setCamFollowElem、getCamFollowElem、cancelCamFollowElem
3. 功能调整：setCamFollowElem替换为setCamTPPElem和setTPPGradeAbility、getCamFollowElem替换为getCamTPPElem和getTPPGradeAbility、cancelCamFollowElem替换为delTPP
4. 相机（Camera）新增接口：createTpp、delTPP、setTPPSportAnimName、getTPPSportAnimName、setTPPIdleAnimName、getTPPIdleAnimName、setTPPGradeAbility、getTPPGradeAbility、setTPPSphereCollider、getTPPSphereCollider、getCamTPPElem、setCamTPPElem、getIsTPP
5. 单构件（Entity）新增接口：getAnimCtlGroupNames、setAnimCtlByGroup、setAnimPosByGroup、getAnimPosByGroup
6. 锚点（Anchor）调整接口：addAnc、addAnimAnc 新增 textBackPadding 属性，设置字体背景内容边距
（注：该版本SDK中“单构件”需配合v3.1.0.3247版本的转换模板使用）

### SDK_V3.2.0.3250 - 2025-07-23

- Title: Web SDK 更新时间：2025.07.23
- SDK package: `Sources/2025_07_23_14_17_58_3a1b481b-5375-ad79-5a18-125ff0388506_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine SDK_v3.2.0.3250.zip`
- API manual: `Sources/2025_07_23_14_17_53_3a1b481b-3f13-f315-73bb-bb20ba645ef0_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine API_Web-v3.2.0.3250.docx`

1. 相机（Camera）新增接口：setCamFollowElem、getCamFollowElem、cancelCamFollowElem
2. 新增了第三人称漫游功能（相机跟随效果）
3. 优化了框选范围不精确的问题
4. 优化了部分单构件显示闪烁的异常
5. 优化了单构件运动时的阴影效果
6. 解决了项目改变仿射变换后造成自定义范围获取数据异常的问题
（注：该版本SDK中“框选范围”需配合v3.1.0.3247版本的转换模板使用）

### SDK_V3.2.0.3220 - 2025-06-27

- Title: Web SDK 更新时间：2025.06.27
- SDK package: `Sources/2025_06_27_14_19_49_3a1ac237-ac8f-e64d-ab49-b5a836623b51_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine SDK_v3.2.0.3220.zip`
- API manual: `Sources/2025_06_27_14_19_40_3a1ac237-8be1-d03e-0aff-ac7b4671e433_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine API_Web-v3.2.0.3220.docx`

1. 修复了BIM（BIM）：getAxisGridRegElem、getPolyFenceRegElem接口数据获取异常的问题
2. 优化了Crtl框选回调事件RESystemFrameSel的触发时机
3. 优化了大批量构件相关的一次性设置操作的调用
4. 电子围栏（Fence）新增接口：getPotInAnyFence

### SDK_V3.2.0.3207 - 2025-06-23

- Title: Web SDK 更新时间：2025.06.23
- SDK package: `Sources/2025_06_23_17_51_52_3a1aae60-6023-2398-3ba6-69c1683eed97_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine SDK_v3.2.0.3207.zip`
- API manual: `Sources/2025_06_23_17_51_41_3a1aae60-3766-d3bf-a0ae-968fcf2b7d74_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine API_Web-v3.2.0.3207.docx`

1. BIM（BIM）调整接口：setElemAttr新增字段useNewAlpha、useNewClr、useNewEmis、useNewSmoothMetal，增加自定义设置各项属性的功能
2. 修复了单构件路径动画添加两点线段的路径动画异常的问题

### SDK_V3.2.0.3200 - 2025-06-17

- Title: Web SDK 更新时间：2025.06.17
- SDK package: `Sources/2025_06_17_17_51_53_3a1a8f7a-3e8d-009b-857d-e71ce22c7a34_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine SDK_v3.2.0.3200.zip`
- API manual: `Sources/2025_06_17_17_51_49_3a1a8f7a-2c15-9294-a67d-8f6988afc1b2_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine API_Web-v3.2.0.3200.docx`

1. 修复了加载时天空盒颜色异常闪烁的问题
2. 优化了CAD特殊符号的支持
3. 修复了360和CAD单独加载不显示的异常问题

### SDK_V3.2.0.3178 - 2025-06-03

- Title: Web SDK 更新时间：2025.06.03
- SDK package: `Sources/2025_06_03_14_21_34_3a1a46a0-a662-a980-2b6f-39b0471fdceb_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine API_Web-v3.2.0.3178.zip`
- API manual: `Sources/2025_06_03_14_21_16_3a1a46a0-6150-119a-8b91-36d737e971e8_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine API_Web-v3.2.0.3178.docx`

1. 修复了加载玩360全景再加载模型天空盒异常的问题
2. 优化了填挖方计算方式，支持地形数据的计算
3. 修复了测量接口调用异常问题
4. 修复了测量贴地线渲染异常问题

### SDK_V3.2.0.3165 - 2025-05-12

- Title: Web SDK 更新时间：2025.05.12
- SDK package: `Sources/2025_05_19_11_51_49_3a19f8d8-2b14-a408-7064-24e26e09bbd6_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine SDK_v3.2.0.3165.zip`
- API manual: `Sources/2025_05_19_11_51_45_3a19f8d8-1bc5-618a-c6cf-4446e736d7eb_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine API_Web-v3.2.0.3165.docx`

1. 相机（Camera）新增接口：exitCamLocating
2. 几何图形（Geometry）调整接口：addPolylineShp新增字段projSce实现矢量线（面）贴地投影功能
3. 几何图形（Geometry）新增接口：setGroupShpProjSce
4. 新增单构件轨迹动画、脚本动画功能
5. 新增粒子效果功能
6. 单构件（Entity）新增接口：getSelfAnimNameList、setAnimPlayModeSingle、setTrackAnim、addAnimScript、delAnimScript、setAnimScriptPlayState、setAnimScriptActive、setAnimScriptStop、getAnimTimeLen
7. 粒子效果（Particle）新增接口：setWeatherSysTex、createWeatherSys、getWeatherSysInfo、getAllWeatherSysIds、delWeatherSys、setTransmitSysTex、getAllTransmitSysIds、delTransmitSys、createTransmitSysPos、getTransmitSysInfoPos、createTransmitSysRect、getTransmitSysInfoRect、addTexGroup、getTexGroupIds、delTexGroup、delAllTexGroup
8. 相机（Camera）新增接口：getCurNorthAngleXOY
9. 新增监听事件：REMeasureFinish

### SDK_V3.2.0.3150 - 2025-05-12

- Title: Web SDK 更新时间：2025.05.12
- SDK package: `Sources/2025_05_14_14_56_26_3a19dfc1-63fb-5d5e-c9df-048b79fdb24e_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine SDK_v3.2.0.3150.zip`
- API manual: `Sources/2025_05_14_14_56_16_3a19dfc1-3c2c-d120-6089-afcab0749309_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine API_Web-v3.2.0.3150.docx`

1. 新增限高分析功能
2. 三维分析（Analysis3D）新增接口：setHeightLimitInfo、getHeightLimitInfo、delHeightLimit、setHeightLimitClr、getHeightLimitClr
3. 修复了测量状态下使用贴地投影模式，角度测量异常的问题

### SDK_V3.2.0.3148 - 2025-05-09

- Title: Web SDK 更新时间：2025.05.09
- SDK package: `Sources/2025_05_12_10_04_41_3a19d469-8ec6-52d9-e239-6426dd4eb93b_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine SDK_v3.2.0.3148.zip`
- API manual: `Sources/2025_05_12_10_04_37_3a19d469-7ff3-350b-686e-db5226800277_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine API_Web-v3.2.0.3148.docx`

1. 测量（Measure）调整接口：移除setSingleStyleState、getSingleStyleState
2. 测量（Measure）调整接口：测量类型调整数值和扩充测量功能
3. 相机（Camera）新增接口：setCamBelowTerrain、getCamBelowTerrain、setCamLockRotate、getCamLockRotate、getConvRotateQ2D、getConvRotateD2Q
4. 新增可视域分析、通视分析功能
5. 三维分析（Analysis3D）新增接口：setViewRegionFovCam、setViewRegionAttrs、addSightLineViewer、getSightLineAllViewerId、getSightLineViewerPos、delSightLineViewer、delSightLineAllViewer、addSightLineTarget、getSightLineAllTargetId、getSightLineTargetPos、getSightLineTargetOccPos、delSightLineTarget、delSightLineAllTarget、setSightLineAttrs
6. 修复了新版谷歌浏览器在Mac系统下遥感影像显示异常的问题
7. 修复了静态阴影图容易产生自阴影的问题
8. 修复了大范围WGS84地形影像转换
9. 地形（Terrain）新增接口：registerPathFunc、unRegisterPathFunc、unRegisterAllPathFunc

### SDK_V3.2.0.3078 - 2025-04-14

- Title: Web SDK 更新时间：2025.04.14
- SDK package: `Sources/2025_04_29_15_53_22_3a1992b6-2059-332e-2b56-81e77c94f424_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine SDK_v3.2.0.3078.zip`
- API manual: `Sources/2025_04_29_15_53_19_3a1992b6-1322-27e6-a613-e542a18ce660_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine API_Web-v3.2.0.3078.docx`

1. 新增三维分析（Analysis3D）模块
2. 三维分析（Analysis3D）新增接口：setSkylineClr、getSkylineClr
3. 解决了球模式下谷歌浏览器加载异常的问题
4. 动画（Animation）调整接口：setShapeAnimStyle参数scaleAndOffset调整缩放系数默认为1.0，调整前为0.0
5. 模型加载（Model）调整接口：loadDataSet中参数wmsInfo的使用

### SDK_V3.2.0.3054 - 2025-03-28

- Title: Web SDK 更新时间：2025.03.28
- SDK package: `Sources/2025_04_02_10_14_56_3a190674-944b-c956-df6c-3f5c9ca0d5c6_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine SDK_v3.2.0.3054.zip`
- API manual: `Sources/2025_04_02_10_14_52_3a190674-82d4-c8c4-9835-a287ca7c585f_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine API_Web-v3.2.0.3054.docx`

1. 优化了CAD部分锚点文字显示不正常问题
2. 优化了局部矢量抗锯齿效果
3. 修复了项目切换时资源对象无法及时释放的问题
4. 新增了对WMS地形服务的支持
5. 模型加载（Model）调整接口：loadDataSet 增加字段 useWMS、wmsInfo，用于加载 WMS 资源服务

### SDK_V3.2.0.3000 - 2025-03-06

- Title: Web SDK 更新时间：2025.03.06
- SDK package: `Sources/2025_03_06_18_09_09_3a187d1b-0933-9153-1e05-f8566e800431_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine SDK_v3.2.0.3000.zip`
- API manual: `Sources/2025_03_06_18_09_01_3a187d1a-e6c2-3634-0436-d9cd4fd83595_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine API_Web-v3.2.0.3000.docx`

1. 新增了控制点配准的位置编辑功能
2. 优化调整了位置编辑功能的使用和界面操作逻辑
3. 模型编辑（Edit）调整接口：startEdit 新增参数字段
4. 模型编辑（Edit）新增接口：getEditState
5. 模型编辑（Edit）移除接口：openAffineTransEditWnd、closeAffineTransEditWnd、setExtendBtnVisible
6. 监听事件新增：REEditControlPosMatchFinish
7. UI工具栏测量模块新增功能面间距、面夹角测量
8. 监听事件移除：REEditAffineTransWndClose
9. 图形显示（Graphics）新增接口：getTabItemVisable、setTabItemVisable
10. 修复了BIM模型GIS坐标变换后包围盒计算错误的问题

### SDK_V3.2.0.2964 - 2025-02-21

- Title: Web SDK 更新时间：2025.02.21
- SDK package: `Sources/2025_03_06_18_05_59_3a187d18-2207-fb92-492d-0bc20e052d5a_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine SDK_v3.2.0.2964.zip`
- API manual: `Sources/2025_03_06_18_05_48_3a187d17-f4ee-8519-a723-eea79490e6d0_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine API_Web-v3.2.0.2964.docx`

1. 剖切（Clip）新增接口：setClipBoxClr、getClipBoxClr、setClipPlaneClr、getClipPlaneClr
2. 优化了CAD渲染效果
3. 解决了设置数据集偏移和坐标系标识时出现坐标异常的情况

### SDK_V3.2.0.2947 - 2025-02-14

- Title: Web SDK 更新时间：2025.02.14
- SDK package: `Sources/2025_03_06_18_05_18_3a187d17-8110-336c-a74c-0e8dbd068bb8_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine SDK_v3.2.0.2947.zip`
- API manual: `Sources/2025_03_06_18_05_08_3a187d17-5ace-45f7-3743-ed2c4e627501_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine API_Web-v3.2.0.2947.docx`

1. 优化了UI工具栏图标的显示效果

### SDK_V3.2.0.2943 - 2025-02-08

- Title: Web SDK 更新时间：2025.02.08
- SDK package: `Sources/2025_03_06_18_04_35_3a187d16-d7c3-cc04-791a-125ea2243904_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine SDK_v3.2.0.2943.zip`
- API manual: `Sources/2025_03_06_18_04_24_3a187d16-ad8c-4310-de85-01aba4e2ea8e_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine API_Web-v3.2.0.2943.docx`

1. 修复了删除自定义坐标系再添加相同标识的坐标系无效的问题

### SDK_V3.2.0.2936 - 2025-01-21

- Title: Web SDK 更新时间：2025.01.21
- SDK package: `Sources/2025_03_06_18_03_13_3a187d15-9a00-9aea-5e89-a9b70feae5ef_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine SDK_v3.2.0.2936.zip`
- API manual: `Sources/2025_03_06_18_03_09_3a187d15-89d3-ff20-081f-d38aa630a525_3a049d33-017c-c541-7c08-bc4bd5e7524a_BlackHole Engine API_Web-v3.2.0.2936.docx`

1. 修复了倾斜摄影资源无法设置属性的问题
2. 优化了UI面板的资源显示
3. 优化了测量数值经度问题

### SDK_V3.2.0.2926 - 2025-01-14

- Title: Web SDK 更新时间：2025.01.14
- SDK package: `Sources/2025_01_15_17_21_04_3a177b71-0827-9a79-e360-5f2314c07cbf_3a044948-7834-ee8f-1ff8-88260d4f3f59_BlackHole Engine SDK_v3.2.0.2926.zip`
- API manual: `Sources/2025_01_15_17_20_56_3a177b70-e9cb-a39d-a2f1-8d478e44b375_3a044948-7834-ee8f-1ff8-88260d4f3f59_BlackHole Engine API_Web-v3.2.0.2926.docx`

1. 优化了对新版地形处理工具处理的数据在操作透明度上的有限支持
2. 地形（Terrain）新增接口：setUnitLayerAlpha、getUnitLayerAlpha、setTerrInstAlpha、getTerrInstAlpha
3. 修复了部分构件使用相机定位无效的问题
4. 优化了单构件渲染效果

### SDK_V3.2.0.2920 - 2025-01-09

- Title: Web SDK 更新时间：2025.01.09
- SDK package: `Sources/2025_01_15_17_20_29_3a177b70-81ab-9207-9264-f5ab7781a439_3a044948-7834-ee8f-1ff8-88260d4f3f59_BlackHole Engine SDK_v3.2.0.2920.zip`
- API manual: `Sources/2025_01_15_17_20_19_3a177b70-5b6e-e874-b920-d82d5a895bf1_3a044948-7834-ee8f-1ff8-88260d4f3f59_BlackHole Engine API_Web-v3.2.0.2920.docx`

1. 优化了部分移动端机型H5无法加载的问题
2. 公共模块（Common）调整接口：addGolFont增加参数antiAliasing
3. 修复了新增的字体设置粗细无效的问题
4. 鼠标探测（Probe）调整接口：getCurProbeRet新增字段elemType、dataSetIdList及相关注释，getCurCombProbeRet接口新增字段dataSetIdList及相关注释
5. 修复了进入测量模式出现异常的问题

### SDK_V3.2.0.2904 - 2024-12-16

- Title: Web SDK 更新时间：2024.12.16
- SDK package: `Sources/2025_01_15_17_19_48_3a177b6f-df8e-3cc4-c4d9-67793f58d4f1_3a044948-7834-ee8f-1ff8-88260d4f3f59_BlackHole Engine SDK_v3.2.0.2904.zip`
- API manual: `Sources/2025_01_15_17_19_34_3a177b6f-a9cf-b07b-a31d-47aa6c843cd5_3a044948-7834-ee8f-1ff8-88260d4f3f59_BlackHole Engine API_Web-v3.2.0.2904.docx`

1. 修复了关闭UI工具栏导致位置编辑窗口关闭的异常情况
2. 修复了H5在部分iPad设备中无法加载的问题
3. 修复了通过UI工具栏隐藏构件，框选依然能够获取选择集列表的异常情况

### SDK_V3.2.0.2901 - 2024-12-10

- Title: Web SDK 更新时间：2024.12.10
- SDK package: `Sources/2025_01_15_17_19_03_3a177b6f-2f88-0403-97f6-53342b637000_3a044948-7834-ee8f-1ff8-88260d4f3f59_BlackHole Engine SDK_v3.2.0.2901.zip`
- API manual: `Sources/2025_01_15_17_18_53_3a177b6f-0b37-8b67-a04b-daafe6c96596_3a044948-7834-ee8f-1ff8-88260d4f3f59_BlackHole Engine API_Web-v3.2.0.2901.docx`

1. 修复了系统工具中的剖切盒异常出现的问题

### SDK_V3.2.0.2897 - 2024-12-09

- Title: Web SDK 更新时间：2024.12.09
- SDK package: `Sources/2025_01_15_17_17_15_3a177b6d-899e-eeeb-d347-41fc469ea008_3a044948-7834-ee8f-1ff8-88260d4f3f59_BlackHole Engine SDK_v3.2.0.2897.zip`
- API manual: `Sources/2025_01_15_17_17_04_3a177b6d-5f8d-0131-6389-cec932e475c6_3a044948-7834-ee8f-1ff8-88260d4f3f59_BlackHole Engine API_Web-v3.2.0.2897.docx`

1. 优化了规则路径动画的贴图效果
2. 几何图形（Geometry）调整接口：addPotShp 新增 useWorldDir、worldRightDir、worldUpDir字段，用于设置二维平面在三维场景下的效果

### SDK_V3.2.0.2890 - 2024-12-03

- Title: 更新时间：2024.12.03
- SDK package: `Sources/202412041500099753a16a2a4-f077-5aa1-79b8-002993cfdcb7BlackHole Engine SDK_v3.2.0.2890.zip`

1. 坐标（Coordinate）新增接口：registerWorldPos、unRegisterWorldPos、unRegisterAllWorldPos
2. 监听事件新增回调：REWorldPosChange
3. 修复了CAD模块中锚点接口文档错误使用的问题
4. 修复了CAD线条、三角面显示的部分异常情况
5. 修复了CAD布局相关使用的异常情况
6. 修复了改变窗口大小导致闪屏的问题
7. 修复了隐藏全部构件操作时，部分构件没有隐藏的问题
8. 动画（Animation）调整接口：addAnimAreaBuffer 参数 texLength 移除，新增参数 policy 设置拐点模式
9. 修复了【Gizmo】当场景和模型设置了坐标系后，旋转编辑模型飞出很远的问题
引擎模块新增接口：setScreenVirRotate、getScreenVirRotate
10. 引擎模块新增接口：setScreenVirRotate、getScreenVirRotate

### SDK_V3.1.0.2828 - 2024-11-08

- Title: Web SDK 更新时间：2024.11.08
- SDK package: `Sources/202411111851329293a162d06-82c1-9ce9-b197-702f79dcadd8BlackHole Engine SDK_v3.1.0.2828.zip`

1. 天空盒（SkyBox）新增接口：setBackImgEnable、getBackImgEnable、setBackImgPath、getBackImgPath、setBackImgFillMode、getBackImgFillMode
2. 动画（Animation）调整接口：setShapeAnimStyle 增加透明度设置功能
3. 相机（Camera）调整接口：setCamLocateToBound 增加入参，设置深度和锁定视角

### SDK_V3.1.0.2816 - 2024-11-01

- Title: Web SDK 更新时间：2024.11.01
- SDK package: `Sources/202411041555550463a160859-3326-40c3-4132-f206a4395366BlackHole Engine SDK_v3.1.0.2816.zip`

1. 测量（Measure）新增接口：getGroupDataByType、getGroupDataByID
2. 测量（Measure）调整接口：addGroupData 允许添加测量集合
3. 修复了在MiniIO模式下，CAD二次加载出现异常的情况

### SDK_V3.1.0.2806 - 2024-10-30

- Title: Web SDK 更新时间：2024.10.30
- SDK package: `Sources/202411011712020723a15f92b-cf18-bd60-d8b8-f4e323bb7084BlackHole Engine SDK_v3.1.0.2806.zip`

1. 公共模块（Common）新增接口：setSceLightAttenu、getSceLightAttenu、setSceAOInfo、getSceAOInfo
2. 修复了设置数据集坐标偏移无效的问题

### SDK_V3.1.0.2803 - 2024-10-25

- Title: Web SDK 更新时间：2024.10.25
- SDK package: `Sources/202410291525509973a15e957-8415-2996-56c5-7e43b12eae0eBlackHole Engine SDK_v3.1.0.2803.zip`

1. CAD（CAD）新增接口：addAreaComment、delAreaComment、setCamLocateToAreaComment
2. H5版本支持球面模式的加载
3. 优化了H5版本UI面板的样式和操作逻辑
4. 修复了CAD部分情况下显示异常的问题
5. 修复了在模型自身有坐标系的情况下编辑位置导致模型异常的问题

### SDK_V3.1.0.2769 - 2024-10-12

- Title: Web SDK 更新时间：2024.10.12
- SDK package: `Sources/202410141728251673a159c88-574f-3a23-d6c0-50ffd9e8542cBlackHole Engine SDK_v3.1.0.2769.zip`

1. 优化了H5版本UI面板样式及功能
2. 修复了Mac平台下Firefox浏览器加载地形显示异常闪烁的问题
3. 相机（Camera）新增接口：getQuatByAxis、getAxisByQuat
4. 修复了CAD在H5模式下不可缩放的问题
5. 优化了CAD部分文字不显示的问题

### SDK_V3.1.0.2748 - 2024-09-14

- Title: Web SDK 更新时间：2024.09.14
- SDK package: `Sources/202409141955171513a150290-051e-aaae-122a-af1aaccc7447BlackHole Engine SDK_v3.1.0.2748.zip`

1. 修复了面板剖切操作异常的问题
2. 修复了某些情况下CAD加载崩溃的问题
3. 修复了位置测量精度和面板设置中测量精度不一致的问题
4. 坐标（Coordinate）新增接口：setCurrSelGeoCoord

### SDK_V3.1.0.2744 - 2024-09-12

- Title: Web SDK 更新时间：2024.09.12
- SDK package: `Sources/202409131014053003a14fb55-8ef4-176a-c6bf-34238c5d9c24BlackHole Engine SDK_v3.1.0.2744.zip`

1. 优化了地形模型的渲染效果
2. 修复了CAD图元图层获取错误的问题
3. 优化了CAD图元显示效果异常的问题

### SDK_V3.1.0.2736 - 2024-08-30

- Title: Web SDK 更新时间：2024.08.30
- SDK package: `Sources/202409021428052493a14c398-2601-b554-0978-bdf9b56f09adBlackHole Engine SDK_v3.1.0.2736.zip`

1. 修复了某些天地图资源无法进行挖洞操作的问题
2. 修复了正交和透视相机模式切换，隐藏状态的viewcube被重置的问题
3. 调整了H5WebSDK的默认渲染模式，打开了阴影光照等渲染效果，性能消耗会有所增加，需要请自行关闭
4. 修复了部分CAD因线条异常无法加载的问题
5. 修复了H5WebSDK在部分苹果设备浏览器查看下无法进行手势操作的问题
6. 优化了部分CAD显示效果

### SDK_V3.1.0.2723 - 2024-08-19

- Title: Web SDK 更新时间：2024.08.19
- SDK package: `Sources/202408290957560113a14ae07-60ab-a36f-cb37-95eb1f010ff5BlackHole Engine SDK_v3.1.0.2723.zip`

1. 修复了MAC平台下鼠标滚轮操作异常的问题
2. 修复了某些情况下UI工具栏测量状态下无法操作的问题
3. 修复了部分情况MAC平台Safar浏览器的瓦片数据显示异常的问题
4. 修复了通过setElemsCanProbe接口设置构件是否探测的情况导致阴影显示异常，以及设置过后鼠标左键平移操作异常的问题
5. CAD（CAD）新增接口：getAllLayoutId、getCurLayoutId、getDefaultLayoutId、setCurShowLayout
6. CAD（CAD）调整接口：addAnc、getAnc、addShpAnc、getShpAnc、getDefaultViewportRange、getCurViewportRange、setCurViewportRange 增加currLayoutId参数，根据不同布局调整效果

### SDK_V3.1.0.2706 - 2024-08-09

- Title: Web SDK 更新时间：2024.08.09
- SDK package: `Sources/202408221012327813a148a08-3d8d-4b3b-0068-cde85e1ede9bBlackHole Engine SDK_v3.1.0.2706.zip`

1. 修复了CAD部分字体的显示错误问题
2. 优化了加载模型和卸载模型之间切换操作的缓存清除机制
3. 优化了系统UI面板操作的交互逻辑

### SDK_V3.1.0.2695 - 2024-08-01

- Title: Web SDK 更新时间：2024.08.01
- SDK package: `Sources/202408201541238653a1480e8-9819-2588-bf7f-eea2f0911044BlackHole Engine SDK_v3.1.0.2695.zip`

1. 修复了在左右分屏的情况下，HDR平均亮度计算没有保持左右两屏统一显示的异常状况
2. 图形显示（Graphics）新增接口：setViewCubeArea、getViewCubeArea
3. 修复了位置编辑窗口设置位置变换信息的缩放只有单轴缩放的异常

### SDK_V3.1.0.2679 - 2024-07-26

- Title: Web SDK 更新时间：2024.07.26
- SDK package: `Sources/202407291633069013a140fcc-0955-fb22-4307-80a79eddf13bBlackHole Engine SDK_v3.1.0.2679.zip`

1. 修复了由于MAC平台没有遵循WebGL std140 常数缓冲区内存布局规范，所导致的MAC浏览器下地形渲染不正常的问题
2. 修复了模型加载时法线没有应用正北夹角的问题
3. 修复了CAD MiniIO资源索引文件释放异常的问题

### SDK_V3.1.0.2655 - 2024-07-19

- Title: Web SDK 更新时间：2024.07.19
- SDK package: `Sources/202407191816406623a13dcab-41d6-3aac-67a4-a7a65a2b452aBlackHole Engine SDK_v3.1.0.2655.zip`

1. 优化了CAD二维图纸的渲染效果
2. 修复了卸载所有数据集没有回调的问题

### SDK_V3.1.0.2633 - 2024-07-10

- Title: Web SDK 更新时间：2024.07.10
- SDK package: `Sources/202407111430113173a13b2a9-0675-5fd8-8230-ac0cfa53103dBlackHole Engine SDK_v3.1.0.2633.zip`

1. BIM（BIM）接口：setSelElemsClr设置颜色时使用当前权重
2. 修复了BIM（BIM）接口：getSelElemsBlendAttr获取子网掩码参数异常的问题
3. 瓦片（Grid）新增接口：setMonomerElemSelEnable、setMonomerElemVisible、delMonomerElem、
4. 瓦片（Grid）移除接口：setShowMonomerElemData、setHideMonomerElemData
5. CAD（CAD）新增接口：getDefaultViewportRange
6. 修复了在部分情况下添加多个倾斜摄影单体化区域会造成重叠的问题

### SDK_V3.1.0.2596 - 2024-06-26

- Title: Web SDK 更新时间：2024.06.26
- SDK package: `Sources/202406271833204043a136b6e-9b14-e5dc-e94d-90106c37338eBlackHole Engine SDK_v3.1.0.2596.zip`

1. 新增灯光（Light）模块
2. 灯光（Light）新增接口：addSpotLights、getSpotLightInfo、getAllSpotLightIds、delSpotLights、delAllSpotLights
3. 坐标系加入了EPSG:3857展开式过滤的功能
4. 调整天空盒（SkyBox）接口setSkyInfo中字段sunDir的使用和注解，放开光源朝向自下向上的限制，主要作用在球面状态，普通场景使用自下向上光源会产生一片漆黑效果

### SDK_V3.1.0.2588 - 2024-06-21

- Title: Web SDK 更新时间：2024.06.21
- SDK package: `Sources/202406241004004913a135a29-386b-4913-82e0-42fca4d94cefBlackHole Engine SDK_v3.1.0.2588.zip`

1. 调整模型加载（Model）接口：loadDataSet的参数terrImgShpAlone改变成groundDisplay

### SDK_V3.1.0.2563 - 2024-06-14

- Title: Web SDK 更新时间：2024.06.14
- SDK package: `Sources/202406141826025863a132875-40da-f562-7937-70b47bad63ccBlackHole Engine SDK_v3.1.0.2563.zip`

1. 修复了锚点同名不同组重复添加不更新的问题

### SDK_V3.1.0.2549 - 2024-06-11

- Title: Web SDK 更新时间：2024.06.11
- SDK package: `Sources/202406111132161353a131787-5a87-4153-7ed9-8be95a016132BlackHole Engine SDK_v3.1.0.2549.zip`

1. 优化了地形渲染模式切换时临时纹理没有释放的问题

### SDK_V3.1.0.2548 - 2024-06-07

- Title: Web SDK 更新时间：2024.06.07
- SDK package: `Sources/202406110937365473a13171e-6123-ed96-377c-ad06f1cfcd4cBlackHole Engine SDK_v3.1.0.2548.zip`

1. 优化了CAD使用上的部分问题

### SDK_V3.1.0.2539 - 2024-06-06

- Title: Web SDK 更新时间：2024.06.06
- SDK package: `Sources/202406071100370703a1302d0-f04e-715b-ed00-ef6670eb3ddfBlackHole Engine SDK_v3.1.0.2539.zip`

1. 修复了360不调用回调的异常
2. 修复了编辑状态下，地形矢量无法选中的问题
3. 修复了大坐标情况下，单构件模型抖动的问题
4. 修复了浏览器缩放窗口会出现黑屏闪烁的问题
5. 优化了CAD的文字编码、缩放比例等
6. 优化了对CAD大文件的支持
7. 地形（Terrain）新增接口：getDataSetTerrId、getTerrSubAllDataSetId
8. 修复了标高无法删除的问题
9. 修复了地形矢量在伪球面模式下无法相机定位的问题

### SDK_V3.1.0.2514 - 2024-05-31

- Title: Web SDK 更新时间：2024.05.31
- SDK package: `Sources/202405311751328583a12e03c-a3fa-2b34-956a-336c0fc8ad79BlackHole Engine SDK_v3.1.0.2514.zip`

1. 优化了地形默认全球影像的展示
2. 修复了cad矢量模型定位问题
3. 模型编辑（Edit）新增接口：setDataSetEditEnable、getDataSetEditEnable
4. 修复了viewcube在部分情况下操作异常的问题

### SDK_V3.1.0.2503 - 2024-05-28

- Title: Web SDK 更新时间：2024.05.28
- SDK package: `Sources/202405281923369483a12d11d-da74-2a42-0f35-1d8085a68999BlackHole Engine SDK_v3.1.0.2503.zip`

1. 支持单独矢量模型在伪球面模式下显示
2. 地形（Terrain）新增接口：setUnitUnitShpHole、getUnitUnitShpHole

### SDK_V3.1.0.2499 - 2024-05-25

- Title: Web SDK 更新时间：2024.05.25
- SDK package: `Sources/202405271055021453a12ca25-e001-16f6-5cfa-8dc07a39af39BlackHole Engine SDK_v3.1.0.2499.zip`

1. 新增地形（Terrain）模块
2. 地形（Terrain）新增接口：getUnitImgShpAlone、setUnitLayerlev、getUnitLayerlev、setUnitActive、getUnitActive、setUnitShpStyleName、getUnitShpStyleName、setUnitUnitOmitParent、getUnitUnitOmitParent、setUnitUnitLODLevRange、getUnitUnitLODLevRange、getAllUnitNames、getUnitBV、getAllShpStyleNames、setShpStyle、getShpStyle、delShpStyle、delAllShpStyle
3. 移除CAD（CAD）中的接口：loadCadShp
4. 模型加载（Model）接口：loadDataSet调整，增加参数，将版本2381之后的CAD.loadCadShp接口功能合并到加载模型Model.loadDataSet接口中，增加地形矢量模型的加载
5. 监听事件新增：RELODLevelChange，监听地形系统矢量LOD分级改变事件
6. 更新名称，栅格名称变更为瓦片，Grid类名不做改变

### SDK_V3.1.0.2478 - 2024-05-11

- Title: Web SDK 更新时间：2024.05.11
- SDK package: `Sources/202405131048428893a128207-0e89-0b53-ebff-cd4c9b567f2fBlackHole Engine SDK_v3.1.0.2478.zip`

1. CAD（CAD）新增接口：setBgClr、getElemsSearchText
2. 修复了在没有传递构件id集合的特定情况下，获取所有构件数据异常的问题

### SDK_V3.1.0.2464 - 2024-05-08

- Title: Web SDK 更新时间：2024.05.08
- SDK package: `Sources/202405091003245783a126d44-2422-167a-e160-f323134b6a74BlackHole Engine SDK_v3.1.0.2464.zip`

1. 相机（Camera）调整接口：setCamLocateToElem、setCamLocateToDataSet 增加自定义视角类型
2. 优化setCamFixCenterPos接口功能
3. 修复某些情况下工具条隔离、隐藏、重置功能切换出现崩溃的问题

### SDK_V3.1.0.2459 - 2024-05-07

- Title: Web SDK 更新时间：2024.05.07
- SDK package: `Sources/202405071520296123a126419-b8ac-3f8f-4597-efe173e38d56BlackHole Engine SDK_v3.1.0.2459.zip`

1. 引擎模块新增接口：setCamModeOnLeftBtnDown、getCamModeOnLeftBtnDown、setCamModeOnRightBtnDown、getCamModeOnRightBtnDown、setCamFixCenterPos、getCamFixCenterPosEnable
2. 公共模块（Common）新增接口：setSceCustomBV、getSceCustomBV
3. 修复viewCube操作定位模型部分超出范围的被工具条遮挡的问题

### SDK_V3.1.0.2434 - 2024-04-12

- Title: Web SDK 更新时间：2024.04.12
- SDK package: `Sources/202404121657047273a11e3b3-29d7-4fa5-d007-19e5db041217BlackHole Engine SDK_v3.1.0.2434.zip`

1. 修复了全局挖洞和全局拍平互斥的问题

### SDK_V3.1.0.2414 - 2024-03-28

- Title: Web SDK 更新时间：2024.03.28
- SDK package: `Sources/202403292031330783a119c5e-7cd6-610b-841c-7a3d5d769fe0BlackHole Engine SDK_v3.1.0.2414.zip`

1. 引擎模块新增接口：setOperationMode、getOperationMode、setCamModeOnMidBtnDown、getCamModeOnMidBtnDown、setCtrlSelectedMode、getCtrlSelectedMode

### SDK_V3.1.0.2394 - 2024-03-15

- Title: Web SDK 更新时间：2024.03.15
- SDK package: `Sources/202403181424256693a116268-6c45-5992-e388-ff0dc2c021b3BlackHole Engine SDK_v3.1.0.2394.zip`

1. 优化了部分CAD显示异常的问题

### SDK_V3.1.0.2381 - 2024-03-08

- Title: Web SDK 更新时间：2024.03.08
- SDK package: `Sources/202403110945224893a113d5c-6d39-41ca-10f6-fd97b39cecedBlackHole Engine SDK_v3.1.0.2381.zip`

1. 引擎模块新增接口：addUrlExtHeader、delAllURLExtHeaders
2. 修复了SDK部分参数异常的情况
3. CAD（CAD）新增接口：loadCadShp
4. 公共模块（Common）新增接口：getSceBV
5. 相机（Camera）新增接口：getCamLocByGISCoord、getGISCoordByCamLoc

### SDK_V3.1.0.2351 - 2024-01-19

- Title: Web SDK 更新时间：2024.01.19
- SDK package: `Sources/202401191818526783a103367-dd86-f3a2-ae53-083c08449cbfBlackHole Engine SDK_v3.1.0.2351.zip`

1. 优化了透明模型的显示效果

### SDK_V3.1.0.2344 - 2024-01-12

- Title: Web SDK 更新时间：2024.01.12
- SDK package: `Sources/202401121744076333a100f3b-88d1-4c3d-884d-8ffcbc475f03BlackHole Engine SDK_v3.1.0.2344.zip`

1. 图形显示（Graphics）新增接口：getSysUIColorStyle
2. 挖洞（Excavate）新增接口：setExcavateEffect、getExcavateEffect
3. 栅格（Grid）新增接口：setTerrSkirtAmp、getTerrSkirtAmp

### SDK_V3.1.0.2331 - 2024-01-05

- Title: Web SDK 更新时间：2024.01.05
- SDK package: `Sources/202401091129422763a0ffe71-a984-18c2-0f3b-cb4557254b7cBlackHole Engine SDK_v3.1.0.2331.zip`

1. 几何图形（Geometry）新增接口：addPolyVolumeShp、addPolyVolumeShpHor
2. 修复REElemSelRegFinish监听事件回调异常的问题

### SDK_V3.1.0.2323 - 2023-12-29

- Title: Web SDK 更新时间：2023.12.29
- SDK package: `Sources/202401091125469873a0ffe6e-126b-6204-84c8-56b22470345eBlackHole Engine SDK_v3.1.0.2323.zip`

1. 优化了局部拍平接口setDataSetFlatRegion的使用，在项目进行了偏移后，依然可以按照项目获取的坐标进行区域填充，而不是需要转换成偏移之前得坐标
2. 修复了CAD标注接口，设置椭圆类型失效的问题

### SDK_V3.1.0.2303 - 2023-12-15

- Title: Web SDK 更新时间：2023.12.15
- SDK package: `Sources/202312151829584553a0f7f33-7237-4c29-0417-07bea41c0d91BlackHole Engine SDK_v3.1.0.2303.zip`

1. 优化了锚点文字显示的区域

### SDK_V3.1.0.2298 - 2023-12-08

- Title: Web SDK 更新时间：2023.12.08
- SDK package: `Sources/202312081754062693a0f5b06-173d-b857-5ab3-1f864039dfaeBlackHole Engine SDK_v3.1.0.2298.zip`

1. 修改了加载minio服务资源发布的cad,360资源时，请求index.xml的路径
2. 修复了模型空间块包围盒无效导致崩溃的问题

### SDK_V3.1.0.2281 - 2023-11-29

- Title: Web SDK 更新时间：2023.11.29
- SDK package: `Sources/202312041049302743a0f44e7-eba2-4005-682f-7e6f466d03caBlackHole Engine SDK_v3.1.0.2281.zip`

1. 修复了锚点无法正常显示的问题
2. 鼠标探测（Probe）新增接口：setCustomProbeExecute
3. 修复了地形项目的包围盒计算问题
4. 修复测试快捷键宏异常问题
5. 优化了地形裙带的显示

### SDK_V3.1.0.2270 - 2023-11-24

- Title: Web SDK 更新时间：2023.11.24
- SDK package: `Sources/202311241926359123a0f1341-bd88-2771-5377-4ff048a1c7f1BlackHole Engine SDK_v3.1.0.2270.zip`

1. 解决了单构件添加动画模式后无法删除的问题
2. 优化了单构件包围盒展示的更新问题
3. 优化了对地形资源生成时的图片边缘处理
4. 相机（Camera）新增接口：setCamLocateToBound
5. 增加了对多层影像叠加资源包的支持
6. 调整了单构件动画的阴影方式
7. 修复了CAD加载单位无效的问题
8. CAD新增接口：unloadCAD
9. 修复了某个全局骨骼层级清空后该层级的骨骼分类统计信息不正确的问题
10. 修复了大坐标时编辑Gizmo抖动的问题
11. 修复了轴心选择按钮对退出编辑行为的状态影响

### SDK_V3.1.0.2226 - 2023-11-10

- Title: Web SDK 更新时间：2023.11.10
- SDK package: `Sources/202311131459467093a0ed9a7-8195-ec63-e8cb-09c2cfec4af9BlackHole Engine SDK_v3.1.0.2226.zip`

1. 单构件（Entity）接口新增：setBVShpVisiable、setBVShpStyle、setBVShpRange
2. 新增监听事件：REAddEntityFinish
3. 优化了与场景遮挡的矢量抗锯齿效果

### SDK_V3.1.0.2214 - 2023-10-27

- Title: Web SDK 更新时间：2023.10.27
- SDK package: `Sources/202311131458007693a0ed9a5-e3c0-2acb-375f-3bc86627fe50BlackHole Engine SDK_v3.1.0.2214.zip`

1. 单构件（Entity）接口调整：删除getXMLEntitys、setXMLEntitys
2. 栅格（Grid）接口调整：删除setDataSetVisible、getDataSetVisible
3. 引擎模块接口新增：addUrlExtParam、delAllURLExtParams
4. 单构件（Entity）新增接口：getTransInfo、setTransInfo
5. 系统UI工具栏增加类型控制，setSysUIWgtVisible接口增加类型PanelBtn_FocusBoxSel
6. 修复部分单构件模型包围盒出现异常的问题
7. 模型编辑（Edit）新增接口：setExtendBtnVisible

### SDK_V3.1.0.2187 - 2023-10-13

- Title: Web SDK 更新时间：2023.10.13
- SDK package: `Sources/202310271031570153a0e8126-3157-e1b5-d945-aeb5520f4085BlackHole Engine SDK_v3.1.0.2187.zip`

1. 增加了对简单渲染模型中的近似的原色保真支持
2. 修复了MiniIO资源下CAD加载无效的问题

### SDK_V3.1.0.2174 - 2023-09-27

- Title: Web SDK 更新时间：2023.09.27
- SDK package: `Sources/202310080941556363a0e1f1f-9134-2867-a50c-e1de2a78f389BlackHole Engine SDK_v3.1.0.2174.zip`

1. 新增CAD（CAD）接口：getCurAllLayer、setLayerVisible、setCamLocateToAllElem、getCurViewportRange、setCurViewportRange、startCommentDraw、endCommentDraw、saveCurCommentDraw、cancelCurCommentDraw、setDrawingCommentStyle、setTextCommentText、setCommentLineWidth、setCommentColor、setCommentTextSize、startMeasurementDraw、endMeasurementDraw、saveCurMeasurementDraw、cancelCurMeasurementDraw、delAllMeasurementDraw、setMeasurementStyle、getLengthMeasurementInfo
2. 新增监听事件：RECADMeasurementDrawFinish
3. 修复了REElemSelRegFinish监听返回异常的问题

### SDK_V3.1.0.2158 - 2023-09-22

- Title: Web SDK 更新时间：2023.09.22
- SDK package: `Sources/202309221812140093a0dce8d-0439-90ba-27a9-6d6df108b98dBlackHole Engine SDK_v3.1.0.2158.zip`

1. 单构件（Entity）调整：删除setCurType、createAnEntity、setAnimPlayMode接口; 以下接口名称调整：getEidtMode->getEditMode、enterEidtMode->enterEditMode、exitEidtMode->exitEditMode
2. 新增单构件（Entity）接口：addEntities、getEntitys、delEntities、getXMLEntitys、setXMLEntitys、setMultiAddEntity、setAnimPlayMode、setMouseAddEntity
3. 新增监听事件：REExitEntityEditMode
4. 名称功能分类调整：Edit.setEditNodeLevel调整为BIM.setSelMode、Edit.getEditNodeLevel调整为BIM.getSelMode、Edit.addDataSetToSel调整为BIM.addToSelDataSet
5. 模型编辑（Edit）调整：删除setEditNodeLevel、getEditNodeLevel、addDataSetToSel接口; startEdit接口增加返回参数
6. 新增BIM（BIM）接口：getSelDataSetIDs、addToSelDataSet、delFromSelDateSets、delAllSelDateSets、setSelMode、getSelMode
7. 名称调整：挤压->挖洞、Extrude->Excavate、extrude->excavate

### SDK_V3.1.0.2139 - 2023-09-08

- Title: Web SDK 更新时间：2023.09.08
- SDK package: `Sources/202309111308205113a0d94d0-d79f-8519-940a-a0d85145e1edBlackHole Engine SDK_v3.1.0.2139.zip`

1. 增加CAD（CAD）的接口：getElemAttrs、getAttrElemIds
2. 增加挤压（Extrude）的接口：addExtrudeFaceTex、clearAllExtrudeFaceTex、createExtrudeObj、delExtrudeObj、setExtrudeType、getExtrudeType、locateToExtrudeObj
3. 解决全景图因为远裁面问题导致不显示的问题
4. 解决了超大范围场景下相机闪烁的问题
5. 修复了部分CAD场景加载错误的问题

### SDK_V3.1.0.2122 - 2023-08-30

- Title: Web SDK 更新时间：2023.08.30
- SDK package: `Sources/202308311622446413a0d5cdc-dea1-7a8a-8601-32ec7f49dfeaBlackHole Engine SDK_v3.1.0.2122.zip`

1. 修复了栅格数据拍平接口setFlatGolRegion在部分情况下无效的问题
2. 增加了对chrome浏览器对天地图资源的支持
3. 修复了单构件显示包围盒不正确的问题

### SDK_V3.1.0.2108 - 2023-08-16

- Title: Web SDK 更新时间：2023.08.16
- SDK package: `Sources/202308161831404233a0d1013-8487-bbda-4e14-a49d20b74a87BlackHole Engine SDK_v3.1.0.2108.zip`

1. 优化了相机的使用，在距离模型过近的情况下，相机穿透的问题
2. 增加单构件（Entity）的接口：getEidtMode、enterEidtMode、exitEidtMode、getAllTypeNames、setCurType、createAnEntity、setAnimPlayMode
3. 优化了系统工具栏中框选放大功能
4. 解决了部分连续管道生成失败的问题，生成中心线回调增加返回信息
5. 优化了部分WMTS类型的资源地址过长时渲染无效的问题

### SDK_V3.1.0.2102 - 2023-08-11

- Title: Web SDK 更新时间：2023.08.11
- SDK package: `Sources/202308161821186333a0d100a-07a9-5c3c-3024-1d1a4a93ff35BlackHole Engine SDK_v3.1.0.2102.zip`

1. 优化了对dwg文件支持包括（优化文字显示，处理属性缺失，增加自定义线型，优化尺寸标注显示，优化块引用加载，优化dwg加载速度等）
2. 优化了轴网裁剪获取构件的适用性，对部分轴网进行了支持
3. 修复正交相机设置无效的问题

### SDK_V3.1.0.2088 - 2023-07-28

- Title: Web SDK 更新时间：2023.07.28
- SDK package: `Sources/202308011045525963a0cc129-ad54-5ca9-b3ca-36d3c4233055BlackHole Engine SDK_v3.1.0.2088.zip`

1. 优化了系统工具栏（框选）相机功能

### SDK_V3.1.0.2087 - 2023-07-21

- Title: Web SDK 更新时间：2023.07.21
- SDK package: `Sources/202307241052276553a0c97fc-d487-57b6-192b-06d26790ba32BlackHole Engine SDK_v3.1.0.2087.zip`

1. 调整几何图形（Geometry）的接口：添加按钮的默认悬浮文字颜色和系统颜色保持统一
2. 优化了360切换延迟问题、调整切换效果
3. 新增系统工具栏功能：增加框选相机定位功能(Ctrl框选)
4. 调整了连续管道选择图片样式

### SDK_V3.1.0.2066 - 2023-07-07

- Title: Web SDK 更新时间：2023.07.07
- SDK package: `Sources/202307111412272173a0c55c1-41d1-00ba-b152-83e24c802650BlackHole Engine SDK_v3.1.0.2066.zip`

1. 增加锚点（Anchor）的接口：setCamToGroupAnc
2. 调整BIM（BIM）接口：getElemAttr的返回参数，增加返回信息
3. 调整几何图形（Geometry）的接口：addPotShp、addPolylineShp、addPolyFenceShp这几个接口增加矢量组字段
4. 增加几何图形（Geometry）的接口：setCamToGroupShp、delGroupShp、getAllGroupName、setGroupShpVisible、getGroupShpVisible、setGroupShpCanOverlap、getGroupShpCanOverlap、setGroupShpVisDist、getGroupShpVisDist、setGroupShpAutoScaleDist、getGroupShpAutoScaleDist
5. 增加360全景（Panorama）的接口：setCamAutoForward
6. 增加监听事件：REPanCamAutoForwardFinish
7. 增加天空盒（SkyBox）的接口：resetSkyInfo
8. 增加BIM（BIM）的接口：setElemUVVisible

### SDK_V3.1.0.2046 - 2023-06-30

- Title: Web SDK 更新时间：2023.06.30
- SDK package: `Sources/202307031418527123a0c2c94-43a8-f9b7-6d64-c779870e7c3dBlackHole Engine SDK_v3.1.0.2046.zip`

1. 修复引擎初始化完成调用Coordinate.getTransGeoCoords接口获取数据异常的问题
2. 新增字段，锚点（Anchor）接口：addAnc新增textBackMode字段
3. 修复了动画（Animation）接口：addAnimAreaBuffer在某些极限情况下动画异常的问题
4. 增加测量（Measure）的接口：getAssistLineVisible、setAssistLineVisible
5. 增加管道（Pipe）的接口：addContPipe、delContPipe、getAllContPipeId、getContPipeElemIDs、setContPipeTex、getContPipeTex、setContPipeClr、getContPipeClr、setShowContPipe、setGenContPipeCenterLine、setCurContPipe、getCurContPipe、saveCurContPipe、resetCurContPipe、removeCurContPipeSubElem、getCurContPipeAllElemIDs、setCurContPipeClr、getCurContPipeClr、startEditContPipeMode、endEditContPipeMode、getContPipeMode、getContPipeInfoXMLStr、setContPipeInfoXMLStr
6. 增加监听事件：REAddContPipeSuccessEvent、REGenPipeCenterLineProgress
7. 增加BIM（BIM）的接口：getElemTransform
8. 增加栅格（Grid）的接口：getDataSetTrans
9. 增加图形显示（Graphics）的接口：resetSysOptStateAndUI

### SDK_V3.1.0.2024 - 2023-06-09

- Title: Web SDK 更新时间：2023.06.09
- SDK package: `Sources/202307031417154983a0c2c92-c7ea-b978-d2d9-7a0cfd6da2c0BlackHole Engine SDK_v3.1.0.2024.zip`

1. 增加鼠标探测（Probe）的接口：setProbeMode、getProbeMode
2. 修复聚合锚点设置文字居中属性无效的问题
3. 增加鼠标栅格（Grid）的接口：setValidState
4. 调整资源文件加载方式，取消了引擎模块接口：initEngineSys的commonUrl的资源地址加载，如果需要预加载模型，可以增加RealBIMWeb.preload.js文件，提升场景模型的初始化渲染速度
5. 修复面积测量模式下投影面积类型设置无效的问题
6. 调整了位置编辑窗口的样式
7. 修复UI 工具条在窗口尺寸改变的情况会下会出现增加问题
8. 调整相机（Camera）接口：setCamLocateToElem、setCamLocateToDataSet，增加locType字段用于在相机对准元素是设置相机的视角，默认当前相机视角

### SDK_V3.1.0.2003 - 2023-06-02

- Title: Web SDK 更新时间：2023.06.02
- SDK package: `Sources/202306061000058783a0ba09b-a3f6-ffc1-d4dc-3fd6e0dcfdd4BlackHole Engine SDK_v3.1.0.2003.zip`

1. 增加鼠标探测（Probe）的接口：setProbeMode、getProbeMode
2. 修复聚合锚点设置文字居中属性无效的问题
3. 增加相机（Camera）的接口：getFreeCamMoveSpeed、setFreeCamMoveSpeed

### SDK_V3.1.0.1998 - 2023-05-29

- Title: Web SDK 更新时间：2023.05.29
- SDK package: `Sources/202306061000010433a0ba09b-9113-d378-01da-11e11915ddf8BlackHole Engine SDK_v3.1.0.1998.zip`

1. 修复系统UI界面初始化不在屏幕中间的问题

### SDK_V3.1.0.1995 - 2023-05-26

- Title: Web SDK 更新时间：2023.05.26
- SDK package: `Sources/202306060959570663a0ba09b-818a-ddbe-0670-23f88e818732BlackHole Engine SDK_v3.1.0.1995.zip`

1. 修复剖切（Clip）接口：getClipState获取数据错误的问题
2. 增加几何图形（Geometry）接口：addPolylineShp的textPos字段增加类型
3. 修复标签（Tag）接口：getTagVisDist获取数据异常的问题
4. 修复锚点（Anchor）接口：getAncVisDist获取数据异常的问题
5. 修复小地图加载图片异常的问题
6. 调整（Model）的接口：loadDataSet的字段originCRS改为engineOrigin
7. 修复了开启位置编辑选中构件出现图标的异常问题
8. 修复了栅格数据加载不同两份出现渲染一样的问题
9. 修复获取选择集数据出现超大构件id的问题

### SDK_V3.1.0.1978 - 2023-05-16

- Title: Web SDK 更新时间：2023.05.16
- SDK package: `Sources/202306060959522053a0ba09b-6e8d-fbfd-29aa-a4aacb5de748BlackHole Engine SDK_v3.1.0.1978.zip`

1. 增加模型加载（Model）的接口：loadDataSet增加字段（dividePrior、originCRS）
2. 监听事件增加：REElevationUpdateFinish、REAxisGridUpdateFinish
3. 修复水面接口调用异常的问题
4. 修复了部分地形转换后无法加载的问题

### SDK_V3.1.0.1970 - 2023-05-12

- Title: Web SDK 更新时间：2023.05.12
- SDK package: `Sources/202306060959427753a0ba09b-49b7-5d7c-b177-5035a19bc50cBlackHole Engine SDK_v3.1.0.1970.zip`

1. 增加坐标（Coordinate）的接口：getValueDispPrecision、setValueDispPrecision
2. 修复了系统UI面板设置坐标精度功能无效的问题
3. 增加相机（Camera）的接口：resetCamLocate
4. 增加图形显示（Graphics）的接口：setPreLoadPicPath
5. 调整BIM（BIM）的接口：setElemAlpha开放可以设置所有数据集
6. 增加动画（Animation）的接口：addAnimCylinder
7. 调整动画（Animation）的接口：addAnimAreaBuffer 增加字段用于设置UV纹理长度

### SDK_V3.1.0.1951 - 2023-05-06

- Title: Web SDK 更新时间：2023.05.06
- SDK package: `Sources/202306060959346353a0ba09b-29eb-c677-fdcd-64d2734ea403BlackHole Engine SDK_v3.1.0.1951.zip`

1. 修复1892之后的版本水面无法加载的异常
2. 修复切换暗色主题，测量模块的坡度显示文字颜色异常的问题
3. 调整自定义天空盒设置，光照方向Z方向不能为正值，即不能从下向上照射
4. 修复添加水面时模型渲染反射异常的问题
5. 增加CAD（CAD）的接口：addFillElem、delFillElem
6. 增加动画（Animation）的接口：addAnimAreaBuffer

### SDK_V3.1.0.1942 - 2023-04-26

- Title: Web SDK 更新时间：2023.04.26
- SDK package: `Sources/202306060959295493a0ba09b-160d-affd-8b4b-7c2e8a2ec0daBlackHole Engine SDK_v3.1.0.1942.zip`

1. 增加剖切（Clip）接口：getBoxClipTransType、setBoxClipTransType、setReverseShowClipRgn、setClipBrowseStyle、setClipEditStyle、resetClip、getClipBrowseState、setLocateToClipPlane、getClipOptState、getSingleClipCreateType、setSingleClipCreateType、setBoxClip、setDataSetBoxClip
2. 增加测量（Measure）接口：setValueDispPrecision、getValueDispPrecision、setSlopeVisible、getMeasureType、setMeasureType、getSingleStyleState、setSingleStyleState、getLengthDataShowType、setLengthDataShowType、getAreaDataShowType、setAreaDataShowType、startMeasureState、endMeasureState、cancelCurPotOpt、getCurState、addGroupData、delGroupData、delTypeData
3. 废弃移除接口：setElemVisible、getElemVisible
4. 调整剖切（Clip）接口：setClipAxisGrid->getAxisGridRegElem从剖切（Clip）调整为BIM（BIM）并调整对应的回调监听函数名称
5. 增加BIM（BIM）接口：getPolyFenceRegElem
6. 增加监听回调接口：REElemSelRegFinish
7. 修复了延迟加载模型导致进度回调监听发出两次成功信息的问题

### SDK_V3.1.0.1934 - 2023-04-19

- Title: Web SDK 更新时间：2023.04.19
- SDK package: `Sources/202306060959232243a0ba09a-fd58-616a-d80f-888f861d9303BlackHole Engine SDK_v3.1.0.1934.zip`

1. 增加BIM（BIM）的接口：setElemUVAnimAttr
2. 增加了MiniIO模式下，CAD和360资源对路径索引文件的支持

### SDK_V3.1.0.1931 - 2023-04-18

- Title: Web SDK 更新时间：2023.04.18
- SDK package: `Sources/202306060959219773a0ba09a-f879-732c-f0ef-a9fd4d2c69c5BlackHole Engine SDK_v3.1.0.1931.zip`

1. 增加轴网（AxisGrid）的接口：delAllData
2. 优化相机朝向四元组和方向向量之间的转换
3. 支持轴网多个点位的添加
4. 增加BIM（BIM）的接口：setBorderLineNorLight、getBorderLineNorLight
5. 解决MiniIO项目路径索引文件失效的问题

### SDK_V3.1.0.1921 - 2023-04-14

- Title: Web SDK 更新时间：2023.04.14
- SDK package: `Sources/202306060959190003a0ba09a-ecd8-661d-e7a4-3668ba5c0b22BlackHole Engine SDK_v3.1.0.1921.zip`

1. 优化CAD文字、坐标、解析dwg速度等
2. 增加移动端剖切操作的基础上进行测量的功能

### SDK_V3.1.0.1918 - 2023-04-12

- Title: Web SDK 更新时间：2023.04.12
- SDK package: `Sources/202306060958588593a0ba09a-9e2b-fd2b-0781-90828c2755c9BlackHole Engine SDK_v3.1.0.1918.zip`

1. 增加公共模块（Common）的接口：getShadowInfo、setShadowInfo
2. 增加图形显示（Graphics）的接口：setSysPanelUIDockArea、createSysPanelBtn、setBtnActiveState、getBtnActiveState、getSysPanelAllChildIds、addSysPanelChildWidget、removeSysPanelWidget、createSysPanelImage、getImagePicPath、setImagePicPath、getBtnStatePicPath、setBtnStatePicPath、delWidget、setSysPanelBtnClrStyle
3. 增加栅格（Grid）的接口：resetDataSetClr
4. 增加模型加载（Model）的接口：getAllDataSetReady、getDataSetReady
5. 修复360相机设置无效的问题
6. 修复相机接口：setCamPreferFPS调用无效的问题
7. 增加相机（Camera）的接口：getCamForcedInitLoc、setCamForcedInitLoc
8. 增加BIM（BIM）的接口：setMaxSmooth、getMaxSmooth
9. 调整场景实时反射默认为关闭
10. 增加标高（Elevation）的接口：setOverlap、getOverlap、delAllData

### SDK_V3.1.0.1892 - 2023-03-22

- Title: Web SDK 更新时间：2023.03.22
- SDK package: `Sources/202306060958481313a0ba09a-7443-1be1-96ef-7bf9a1912d78BlackHole Engine SDK_v3.1.0.1892.zip`

1. 修复了设置选择集颜色，位置编辑时栅格类型模型颜色异常问题

### SDK_V3.1.0.1891 - 2023-03-21

- Title: Web SDK 更新时间：2023.03.21
- SDK package: `Sources/202306060958455933a0ba09a-6a59-5cf7-bc79-d6e2c8365434BlackHole Engine SDK_v3.1.0.1891.zip`

1. 增加公共模块（Common）的接口：getCurRenderStateData、setCurRenderStateData
2. 增加图形显示（Graphics）的接口：resetInitialState
3. 修复相机（Camera）接口：setCamLocateTo 运动速度设置无效的问题
4. 修复相机（Camera）接口：setCamLocateDefault调用无效问题

### SDK_V3.1.0.1888 - 2023-03-20

- Title: Web SDK 更新时间：2023.03.20
- SDK package: `Sources/202306060958384523a0ba09a-4e74-7723-0d49-dbd3eaf46af2BlackHole Engine SDK_v3.1.0.1888.zip`

1. 调整了模块层次，增加动画（Animation）模块，原BIM.动画与特效接口，修改了部分接口名称，涉及接口：addAnimationWall->addAnimWall、addAnimationPlane->addAnimPlane、addAnimationSpheres->addAnimSpheres、addAnimationPolygons->addAnimPolygons、addAnimationPolygonWalls->addAnimPolygonWalls
2. 增加栅格（Grid）的接口：getSurplusID、getData、setDataIntoClip、setData、endClip、getClipState、setSingleClip、setClipSpecifyHeight、setLocateToClipElem、setClipAxisGrid
3. 增加小地图（MiniMap）的接口：getVisible、setVisible、setBackClr、setShowRangeRefresh、loadCAD、loadImage、getRegion、setRegion、getMaxRegion、setMaxRegion、getMinRegion、setMinRegion、setIconStyle、setCamLocateTo、getConvertCamTransInfo、setConvertCamTransInfo、setCamTransInfo、getCamTransInfo、setCADGroupShpAncScale、addCADShpAnc、getCADShpAncNum、getAllCADShpAnc、getCADShpAnc、getAllCADShpAncGroupIDs、getCADGroupShpAnc、delAllCADShpAnc、delCADShpAnc、delCADGroupShpAnc
4. 修改小地图监听回调名称：RealBIMLoadMinMapCAD->REMiniMapLoadCAD、RealBIMSelCADMinMapShpAnchor->REMiniMapCADSelShpAnchor

### SDK_V3.1.0.1880 - 2023-03-16

- Title: Web SDK 更新时间：2023.03.16
- SDK package: `Sources/202306060958248043a0ba09a-1924-b1a3-224d-25fb0768cdf3BlackHole Engine SDK_v3.1.0.1880.zip`

1. 增加标注（Mark）的接口：startAdd、setText、getCurData、endAdd、showData
2. 添加有限元加载完成监听事件：RELoadFEMFinish
3. 增加有限元（FEM）的接口：loadData、removeData、getAllScalarParamName、setActiveScalar、setCLUT
4. 增加轴网（AxisGrid）的接口：setData、getAllGroupNames、getGuid、delData、setClr、setProbeEnable、setVisible、setOverlap、getOverlap
5. 增加BIM接口：setSelElemsBlendAttr、getSelElemsBlendAttr 设置选择集的混合属性
6. 修改BIM.动画与特效接口：setShapeAnimStyle的入参模型
7. 增加标高（Elevation）的接口：setData、getAllGroupNames、getGuid、delData、setClr、setProbeEnable、setVisible、getData
8. 增加测量（Measure）的接口：startShowFenceMinDis、endShowFenceMinDis、drawHoriDisLine、clearHoriDisLine、drawDisLine、clearDisLine、setLineClr、setTextStyle、resetDefaultStyle
9. 增加电子围栏（Fence）的接口：startFenceEdit、addFence、endAddFence、endFenceEdit、setPicStyle、getAllPotInfo、getFenceName、delFencePot、delFence、delAllFence、addFenceByPot
10. 增加引擎模块接口：getScreenSnapshot屏幕快照

### SDK_V3.1.0.1873 - 2023-03-13

- Title: Web SDK 更新时间：2023.03.13
- SDK package: `Sources/202306060958211403a0ba09a-0ad4-200a-ccc4-4ea769f98b99BlackHole Engine SDK_v3.1.0.1873.zip`

1. 增加倾斜摄影拍平接口：setFlatRegionEffective、getFlatRegionEffective、clearLocalFlatRegion、setLocalFlatRegionEffective、getLocalFlatRegionEffective
2. 增加倾斜摄影单体化接口：setMonomerElemData、setShowMonomerElemData、setHideMonomerElemData、addToSelMonomerElemIDs、removeFromSelMonomerElemIDs、getSelMonomerElemIDs、setSelMonomerElemClr、setMonomerElemHideClr
3. 增加360全景（Panorama）接口：setCamLocateToDestPos、getCamLocate、getCurShpProbeRet、getTexPos、addAnc、getAllAncName、delAnc
4. 增加水面（Water）接口：loadData、getData、delData、delAllData、setCamToData
5. 增加引擎模块接口：getCamRevLR、setCamRevLR、getEscKeyExitOpEnable、setEscKeyExitOpEnable
6. 增加相机模块的碰撞检测接口：setCamCollideState、getCamCollideState
7. 增加相机模块的重力模拟接口：setCamGravityState、getCamGravityState、setCamGravityHeight、getCamGravityHeight
8. 调整了栅格（Grid）接口：setGroupAlpha->setDataSetAlpha、getGroupAlpha->getDataSetAlpha、setGroupDepthBias->setDataSetDepthBias的名称
9. 增加栅格（Grid）的渲染设置接口：refreshDataSet、setDataSetClr、setDataSetVisible、getDataSetVisible、setDataSetTrans、getDataSetBV
10. 增加CAD的接口：setCamLocateToElem、selElem、addAnc、getAnc、getAncNum、getAllAnc、delAnc、delAllAnc、addShpAnc、getShpAnc、getShpAncNum、getAllShpAnc、delShpAnc、delAllShpAnc、getAllShpAncGroupIDs、getGroupShpAnc、delGroupShpAnc、setGroupShpAncScale

### SDK_V3.1.0.1870 - 2023-03-06

- Title: Web SDK 更新时间：2023.03.06
- SDK package: `Sources/202306060958024083a0ba099-c1a8-6563-bf76-81ea9d4bf466BlackHole Engine SDK_v3.1.0.1870.zip`

1. 调整了接口：setFixDataSetCam的接口名称为setFixCurCam
2. 调整了接口：getGolFont的返回参数，去除了部分参数

### SDK_V3.1.0.1857 - 2023-03-03

- Title: Web SDK 更新时间：2023.03.03
- SDK package: `Sources/202306060950493703a0ba093-261a-4b54-800d-89eeee3a8a5dBlackHole Engine SDK_v3.1.0.1857.zip`

1. 调整了接口：refreshAllDataSet的调用层级，从BIM层级变更为Model层级

### SDK_V3.1.0.1852 - 2023-03-03

- Title: Web SDK 更新时间：2023.03.03
- SDK package: `Sources/202306060948593643a0ba091-7864-c752-2180-fee8c66ce373BlackHole Engine SDK_v3.1.0.1852.zip`

1. 调整了构件属性接口的使用，将setElemClr、setElemBlendAttr接口整合为setElemAttr，调整传参方式，改用对象，各字段为选填字段
2. 调整了构件属性接口的使用，将resetElemBlendAttr、resetElemAttr接口整合为resetElemAttr，字段不变，功能整合
3. 调整了构件属性接口的使用，将getElemClr名称调整为getElemAttr，不改变使用方式
4. 构件属性接口：setElemAlpha新增字段alphaWeight（权重），用于在模型中有透明元素时，可以只用权重辅助进行显示和隐藏

### SDK_V3.1.0.1848 - 2023-02-28

- Title: Web SDK 更新时间：2023.02.28
- SDK package: `Sources/202306060947338923a0ba090-2a84-28d6-8fed-79b6255e4815BlackHole Engine SDK_v3.1.0.1848.zip`

1. 调整了接口：getElemTotalBV、getTotalBV的层级，从坐标层级调整到BIM.构件属性层级
2. 调整了接口名称：setClipPlanesBlendContourLineClr->setClipPlanesContourLineClr、getClipPlanesBlendContourLineClr->getClipPlanesContourLineClr
3. 调整了接口：setClipPlanesContourLineClr的入参字段名称blendClr->lineClr

### SDK_V3.1.0.1845 - 2023-02-23

- Title: Web SDK 更新时间：2023.02.23
- SDK package: `Sources/202306060944341923a0ba08d-6c90-973f-a194-f75606bbe838BlackHole Engine SDK_v3.1.0.1845.zip`

1. 更新了WebSDK 3.0 版本

## Maintenance Rule

- Keep only the latest full API reference Markdown file.
- Do not keep full historical API Markdown snapshots.
- Refresh this file from the source API when the user asks about recent/latest updates or SDK-specific errors.
- If the latest API reference lacks details for a newly added interface, say the interface is listed in upgrade notes but the detailed API section is not present in the bundled API reference.
