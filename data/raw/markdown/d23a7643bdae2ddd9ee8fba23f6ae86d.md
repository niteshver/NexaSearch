![Hugging Face's logo](https://huggingface.co/front/assets/huggingface_logo-noborder.svg) Hugging Face⟨1⟩
  *  Models ⟨2⟩
  *  Datasets ⟨3⟩
  *  Spaces ⟨4⟩
  *  Buckets new⟨5⟩
  *  Docs ⟨6⟩
  *  Enterprise ⟨7⟩
  * Pricing⟨8⟩
  *     * Website
      *  Tasks⟨9⟩
      *  HuggingChat⟨10⟩
      *  Collections⟨11⟩
      *  Languages⟨12⟩
      *  Organizations⟨13⟩
    * Community
      *  Blog⟨14⟩
      *  Posts⟨15⟩
      *  Daily Papers⟨16⟩
      *  Hardware⟨17⟩
      *  Learn⟨18⟩
      *  Discord⟨19⟩
      *  Forum⟨20⟩
      *  GitHub⟨21⟩
    * Solutions
      *  Team & Enterprise⟨7⟩
      *  Hugging Face PRO⟨22⟩
      *  Enterprise Support⟨23⟩
      *  Inference Providers⟨24⟩
      *  Inference Endpoints⟨25⟩
      *  Storage Buckets⟨5⟩
  * * * *
  * Log In⟨26⟩
  * Sign Up⟨27⟩


#   Datasets:⟨3⟩
* * *
 ![](https://huggingface.co/avatars/871ea312b497e55e40fadc1af87b6269.svg) ⟨28⟩
LinkQQ⟨28⟩
/
CoalBench⟨29⟩
like 0
Modalities:  Text ⟨30⟩
Formats:  json ⟨31⟩
Size:  1K - 10K ⟨32⟩
Libraries:  Datasets ⟨33⟩ pandas ⟨34⟩ Polars ⟨35⟩ + 1
License:
cc-by-4.0
 Dataset card ⟨29⟩ Data Studio ⟨36⟩ Files Files and versions xet ⟨37⟩ Community 1 ⟨38⟩
Dataset Viewer
 Auto-converted to Parquet⟨39⟩ API Embed  Duplicate⟨40⟩ Data Studio
Subset (8)
full-en · 742 rows
full-en (742 rows) dpo-en (742 rows) dpo-zh (526 rows) full-zh (526 rows) rar-en (742 rows) rar-zh (526 rows) sft-en (742 rows) sft-zh (526 rows)
Split (1)
train · 742 rows
train (742 rows)
SQL
Console  
|  id int64 0 759  |  class stringclasses 26 values  |  question stringlengths 15 331  |  answer1 stringlengths 2 2.71k  |  answer2 stringlengths 150 3.02k  |  rubrics listlengths 7 20  |  
| --- | --- | --- | --- | --- | --- |  
|  0  |  Ground Control  |  How has the shield support contributed to the improvements in safety and productivity in longwall mining?  |  The shield support has contributed to improvements in safety and productivity in longwall mining by providing unprecedented capacity and stability in a hydraulic support structure, which has remained largely unchanged in its basic design.  |  Shield supports improve safety and productivity in longwall mining by using powered hydraulic systems to provide immediate roof support at the longwall face. As mining progresses, the shields advance with the working face, preventing roof collapse and controlling strata movement. This stable and continuously supported ...  |  [ { "rubric_id": 1, "title": "Hydraulic Roof Support Mechanism", "description": "Essential: Identifies that shield supports use powered hydraulic systems to provide immediate roof support at the longwall face.", "weight": 5 }, { "rubric_id": 2, "title": "Advancing Shield Operation", "d...  |  
|  1  |  Ground Control  |  How did the integration of electrohydraulic control systems enhance the functionality of shield control in mining operations?  |  The integration of electrohydraulic control systems enhanced the functionality of shield control in mining operations by improving precision, responsiveness, and automation, leading to increased safety, efficiency, and productivity in tunneling and excavation processes.  |  Electrohydraulic control systems enhanced shield control in mining operations by automating the support function, enabling a shearer-initiated shield advance capability through location sensing, and providing programmable and consistent setting force across the face. Initially, full setting pressure was not consistentl...  |  [ { "rubric_id": 1, "title": "Automation of Support Function", "description": "Essential: Correctly identifies automation as a core enhancement to shield control.", "weight": 4 }, { "rubric_id": 2, "title": "Shearer-Initiated Shield Advance", "description": "Essential: Explains shearer...  |  
|  2  |  Ground Control  |  What are some key advantages and challenges associated with using steel as a material for mining props?  |  **Advantages of using steel for mining props:** 1. **High strength and durability** – Steel can withstand heavy loads and harsh underground conditions. 2. **Longer lifespan** – Compared to timber, steel props last longer and require less frequent replacement. 3. **Reusability** – Steel props can be retrieved, cleaned,...  |  Steel props offer consistent and predictable structural behavior, making them ideal for creating rigid supports in mining operations. A key advantage is their well-understood mechanical properties, which allow for reliable engineering designs. However, a major challenge lies in achieving the necessary yielding performa...  |  [ { "rubric_id": 1, "title": "Structural Consistency", "description": "Essential: Identifies steel's consistent structural behavior as a key advantage.", "weight": 4 }, { "rubric_id": 2, "title": "Predictable Behavior", "description": "Essential: Mentions predictable performance for mi...  |  
|  3  |  Ground Control  |  How did advancements in shield design and operational capabilities contribute to the improvements in longwall mining safety and productivity?  |  Advancements in shield design and operational capabilities have significantly improved longwall mining safety and productivity by providing better roof support, reducing the risk of roof falls, enabling faster and more efficient coal extraction, and allowing for safer working conditions by minimizing manual interventio...  |  Advancements in shield design and operational capabilities significantly contributed to improvements in longwall mining safety and productivity by enabling higher shield capacities through mature two-leg designs and large-diameter hydraulic cylinders, enhancing structural integrity through experience, testing, and nume...  |  [ { "rubric_id": 1, "title": "Shield Design Advancements", "description": "Essential: Identifies mature two-leg designs and large hydraulic cylinders as key innovations.", "weight": 4 }, { "rubric_id": 2, "title": "Structural Integrity Improvements", "description": "Essential: Explains...  |  
|  4  |  Ground Control  |  In order to effectively solve ground control problems, what fundamental structural engineering principles should be understood first, aside from the associated mathematics?  |  1. Soil mechanics and geotechnical behavior 2. Load distribution and bearing capacity 3. Stability and equilibrium of structures 4. Material properties and failure mechanisms 5. Foundation design and settlement control 6. Retaining wall and slope stability principles 7. Groundwater and its impact on soil st...  |  Prior to describing actual field examples, it is necessary to briefly present a number of structural engineering principles in terms of fundamental mechanics, rather than the associated mathematics, that can be used in ground control problem-solving.  |  [ { "rubric_id": 1, "title": "Stress Concepts", "description": "Essential: Accurately defines stress and its role in structural integrity.", "weight": 4 }, { "rubric_id": 2, "title": "Strain Principles", "description": "Essential: Explains strain relationships in material deformation."...  |  
|  5  |  Ground Control  |  What factors influence the strength characteristics of pillars in coal mining, particularly for main development pillars and chain pillars?  |  The strength characteristics of pillars in coal mining, particularly for main development pillars and chain pillars, are influenced by the following factors: 1. **Pillar Dimensions** – Width and height of the pillar significantly affect its strength. Larger pillars generally have higher strength. 2. **Coal Properties...  |  The strength characteristics of pillars in coal mining, particularly for main development pillars and chain pillars, are influenced by the strength properties of the surrounding strata, the geometry of the pillars, and the stress path or boundary conditions of the pillar system. Main development pillars are limited by ...  |  [ { "rubric_id": 1, "title": "Strata Strength", "description": "Essential: Identifies the strength properties of surrounding strata as a critical factor.", "weight": 4 }, { "rubric_id": 2, "title": "Pillar Geometry", "description": "Essential: Explains how pillar dimensions and shape a...  |  
|  6  |  Ground Control  |  What measures can be taken to protect buildings from damage caused by surface subsidence and deformation resulting from underground coal mining activities in Chinese coal mines?  |  To protect buildings from damage caused by surface subsidence and deformation from underground coal mining in Chinese coal mines, the following measures can be taken: 1. **Mine Planning and Design Optimization** - Implement selective mining techniques to avoid critical areas. - Use pillar-and-stall or longwall...  |  To protect buildings from damage caused by surface subsidence and deformation resulting from underground coal mining activities in Chinese coal mines, the following measures can be taken: 1. **Appropriate Mining Methods**: Employ mining techniques that reduce or control surface movement and deformation. This includes:...  |  [ { "rubric_id": 1, "title": "Mining Methods", "description": "Essential: Includes controlled caving, staggered mining, or protective pillars to manage subsidence.", "weight": 4 }, { "rubric_id": 2, "title": "Structural Reinforcement", "description": "Essential: Mentions foundation rei...  |  
|  7  |  Underground Mining  |  What are the major partial mining methods?  |  The major partial mining methods include: 1. **Room and Pillar Mining** 2. **Longwall Mining** 3. **Retreat Mining** 4. **Block Caving** 5. **Sublevel Caving** 6. **Shrinkage Stope Mining** 7. **Cut-and-Fill Mining** 8. **Open Stope Mining** 9. **Panel Mining** 10. **Slice Mining**  |  The major partial extraction methods in coal mining are strip pillar mining, Wongawilli strip pillar mining, conventional room-and-pillar mining, and thickness-limited extraction. These methods recover only part of the seam or panel so that remnant coal can continue to provide regional or local strata support.  |  [ { "rubric_id": 1, "title": "Strip Pillar Mention", "description": "Essential: Correctly identifies strip pillar mining as a major partial method.", "weight": 4 }, { "rubric_id": 2, "title": "Wongawilli Method", "description": "Essential: Includes Wongawilli strip pillar mining as a d...  |  
|  8  |  Ground Control  |  What specific types of technologies are included in mining damage and protection technology for buildings (structures)?  |  The specific types of technologies included in mining damage and protection technology for buildings (structures) are: 1. **Ground Movement Prediction Models** – Used to forecast subsidence and ground deformation caused by underground mining. 2. **Mine Subsidence Monitoring Systems** – Technologies such as GPS, InSAR ...  |  Mining damage and protection technology for buildings and structures generally includes three categories: reinforcement protection measures, maintenance and strengthening technologies, and anti-mining or mining-resistant structural design. Together, these technologies aim to reduce subsidence-induced deformation, impro...  |  [ { "rubric_id": 1, "title": "Reinforcement Protection", "description": "Essential: Correct identification of reinforcement protection measures for buildings.", "weight": 4 }, { "rubric_id": 2, "title": "Maintenance Enhancement", "description": "Essential: Accurate mention of maintenan...  |  
|  9  |  Ground Control  |  What specific reinforcement protection measures are typically employed for buildings when mining operations are conducted beneath them?  |  The specific reinforcement protection measures typically employed for buildings when mining operations are conducted beneath them include: 1. **Underpinning** – Strengthening the building foundations by extending them to a more stable soil layer or bedrock. 2. **Piling** – Installing deep foundation piles to transfer ...  |  Typical reinforcement protection measures for buildings above underground coal mining include crack-control treatment, high-strength steel tie rods, reinforced concrete beams, horizontal sliding layers, double-plate foundations, deformation-compensation trenches, surface compensation grouting, and sand pumping or backf...  |  [ { "rubric_id": 1, "title": "Deformation Cracks", "description": "Essential: Correctly identifies deformation cracks as a primary protection measure.", "weight": 3 }, { "rubric_id": 2, "title": "High Strength Steel Rods", "description": "Essential: Mentions high strength steel rods fo...  |  
|  10  |  Ground Control  |  What types of maintenance and enhancement technologies are used to protect buildings from damage caused by coal mining?  |  The types of maintenance and enhancement technologies used to protect buildings from damage caused by coal mining include: 1. **Ground Movement Monitoring Systems** – Such as automated inclinometers, piezometers, and GPS sensors to detect subsidence and ground deformation. 2. **Underpinning Techniques** – Including m...  |  The types of maintenance and enhancement technologies used to protect buildings from damage caused by coal mining include beam reinforcement technology, foundation adjustment and replacement technology, and wall-reinforcement technology. Methods such as chemical grouting, cement grouting, or concrete injection are used...  |  [ { "rubric_id": 1, "title": "Beam Reinforcement", "description": "Essential: Identifies beam reinforcement technology as a core method for structural protection.", "weight": 4 }, { "rubric_id": 2, "title": "Foundation Adjustment", "description": "Essential: Mentions foundation adjustm...  |  
|  11  |  Others  |  What specific measures are included in resisting mining design technology for buildings?  |  Resisting mining design technology for buildings typically includes the following specific measures: 1. **Reinforced Structural Design** – Using stronger materials and structural systems to withstand ground vibrations and subsidence caused by mining activities. 2. **Flexible Foundations** – Designing foundations that...  |  Resisting mining design technology for buildings includes the determination of buildings locations and the treatment technology for the foundation. Reconstruction of antideformation buildings on the top of the gob has been applied. New houses are all strip foundation, brick walls, or precast concrete hollow floor. The ...  |  [ { "rubric_id": 1, "title": "Location Determination", "description": "Essential: Correctly identifies building location assessment as a core measure.", "weight": 4 }, { "rubric_id": 2, "title": "Foundation Treatment", "description": "Essential: Mentions foundation treatment technology...  |  
|  13  |  Ground Control  |  What are the primary operational options for reducing longwall-induced stresses in the sandstone and the longwall abutment pressures within the gateroad pillars when considering fixed geologic parameters such as the depth of cover, potential caving height, sandstone interval, and sandstone strength?  |  The primary operational options for reducing longwall-induced stresses in the sandstone and the longwall abutment pressures within the gateroad pillars include: 1. **Optimizing longwall mining geometry** – Adjusting the longwall face length, panel width, and mining sequence to control stress distribution and reduce ab...  |  When geological parameters such as cover depth, caving height, sandstone interval, and sandstone strength are fixed, the main operational controls are to adjust longwall panel width and redesign the gateroad pillars. Panel-width changes modify the distribution of abutment stresses, while pillar design changes improve t...  |  [ { "rubric_id": 1, "title": "Panel Width Adjustment", "description": "Essential: Correctly identifies changing panel width as a primary operational option to reduce longwall-induced stresses.", "weight": 4 }, { "rubric_id": 2, "title": "Gateroad Pillar Design", "description": "Essenti...  |  
|  14  |  Ground Control  |  What role does pre- or post-tensioning play in the effectiveness of tension cable bolts used for supporting roofs in mining applications?  |  Pre- or post-tensioning increases the effectiveness of tension cable bolts by applying compressive forces to the surrounding rock, improving stability, reducing movement, and enhancing the load-bearing capacity of the roof in mining applications.  |  Pre- or post-tensioning plays a critical role in the effectiveness of tension cable bolts by creating an active force on the bearing plate, which enhances support performance by providing confinement and reducing roof deformation. This pre-load helps maintain the roof in a state of compression, similar to pre-tensioned...  |  [ { "rubric_id": 1, "title": "Active Force Bearing Plate", "description": "Essential: Correctly identifies pre/post-tensioning creates active force on the bearing plate.", "weight": 4 }, { "rubric_id": 2, "title": "Confinement and Deformation", "description": "Essential: Explains how a...  |  
|  15  |  Underground Mining  |  What are thick coal seams?  |  Thick coal seams are layers of coal in the earth that are relatively deep and have a significant vertical thickness, often ranging from several meters to tens of meters. They are important sources of coal for mining due to their high volume and accessibility.  |  Thick coal seams refer to those with a seam thickness greater than 3.5 meters. There are several countries with thick coal seam resources, including China, United States, Australia, Poland, and India. China has abundant resources of thick coal seams. Both the reserve and production of thick seam coals account for a sig...  |  [ { "rubric_id": 1, "title": "Definition Accuracy", "description": "Essential: Correctly defines thick coal seams as exceeding 3.5 meters in thickness.", "weight": 4 }, { "rubric_id": 2, "title": "Geographic Scope", "description": "Essential: Lists at least three countries with signifi...  |  
|  16  |  Ground Control  |  How does the stability control of large-cutting-height shield encompass both the stability of a single shield and the stability of a group of shields?  |  The stability control of large-cutting-height shield encompasses both the stability of a single shield and the stability of a group of shields by integrating structural reinforcement, real-time monitoring, coordinated control systems, and geological adaptation. This ensures individual shield integrity while maintaining...  |  Stability control for large-cutting-height shield supports involves both single-shield stability and the stability of the shield group. From a shield-design perspective, destabilizing factors should be reduced by increasing setting load and support capacity, using larger-bore hydraulic legs where feasible, widening the...  |  [ { "rubric_id": 1, "title": "Single Shield Stability", "description": "Essential: Correctly identifies the need to improve single shield stability through design factors like setting load and support capacity.", "weight": 5 }, { "rubric_id": 2, "title": "Group Shield Stability", "desc...  |  
|  17  |  Ground Control  |  What specific features do the face guards and extension canopies have in terms of anti-face spalling characteristics for the shields?  |  The face guards and extension canopies are designed with anti-face spalling characteristics that include impact-resistant materials, reinforced structural layers, and energy-absorbing components to prevent fragmentation and maintain integrity under high-velocity or high-impact conditions.  |  The face guards and extension canopies of the shields have the following specific features in terms of anti-face spalling characteristics: 1. **Solid Top Canopy with Large Stroke Extension Canopy**: Ensures good top protection capability. 2. **Two-Stage Face Guard (Retractable and Stretchable)**: - The front end of ...  |  [ { "rubric_id": 1, "title": "Solid Top Canopy", "description": "Essential: Identifies the solid top canopy with large stroke extension as a core anti-spalling feature.", "weight": 4 }, { "rubric_id": 2, "title": "Two-Stage Mechanism", "description": "Important: Describes the two-stage...  |  
|  18  |  Carbon Reduction and Circular Utilization  |  What percentage of the world's total recoverable coal reserves does Eastern Europe and the FSU have?  |  Eastern Europe and the FSU have approximately 25% of the world's total recoverable coal reserves.  |  Eastern Europe and the former Soviet Union account for approximately 27 percent of the world's total recoverable coal reserves. The value should be understood as a regional share of recoverable reserves, not as total coal resources in place.  |  [ { "rubric_id": 1, "title": "Correct Percentage", "description": "Essential: States the exact percentage (27%) required for this answer.", "weight": 5 }, { "rubric_id": 2, "title": "Region Mention", "description": "Essential: Explicitly names both Eastern Europe and the FSU as the reg...  |  
|  19  |  Carbon Reduction and Circular Utilization  |  What percentage of the world's recoverable coal reserves does the Middle East, Asia, and Oceania region contain?  |  The Middle East, Asia, and Oceania region contain approximately 28% of the world's recoverable coal reserves.  |  The Middle East, Asia, and Oceania region contains approximately 31 percent of the world's recoverable coal reserves. This percentage refers to the combined regional share of recoverable reserves rather than a single-country coal reserve estimate.  |  [ { "rubric_id": 1, "title": "Correct Percentage", "description": "Essential: States the exact percentage (31%) required for this answer.", "weight": 5 }, { "rubric_id": 2, "title": "All Three Regions Mentioned", "description": "Important: Explicitly names the Middle East, Asia, and Oc...  |  
|  20  |  Carbon Reduction and Circular Utilization  |  What factors influence the selection of coal combustion systems, and can you describe the three primary types of coal combustion methods: fixed bed, fluidized bed, and suspension firing?  |  Factors influencing the selection of coal combustion systems include coal type, sulfur content, ash content, boiler size, emission regulations, fuel flexibility, and efficiency requirements. 1. **Fixed Bed Combustion**: Coal is burned on a stationary bed, typically in a grate or retort. Air is supplied from below, and...  |  The selection of coal combustion systems is influenced by the desired unit size or capacity (i.e., required hourly steam production or electricity generation) and coal type and quality. The three primary types of coal combustion methods are: 1. **Fixed Bed (Stokers):** Coal is burned on a grate or bed, where air is su...  |  [ { "rubric_id": 1, "title": "Unit Size/Capacity", "description": "Essential: Identifies the influence of required hourly steam production or electricity generation on system selection.", "weight": 4 }, { "rubric_id": 2, "title": "Coal Type/Quality", "description": "Essential: Explains...  |  
|  21  |  Carbon Reduction and Circular Utilization  |  What are the primary benefits of using gasification as a process for upgrading solid feedstocks, particularly in terms of handling, environmental impact, and fuel efficiency?  |  The primary benefits of using gasification for upgrading solid feedstocks include improved handling due to conversion into a more manageable gaseous form, reduced environmental impact through lower emissions and the potential for carbon capture, and enhanced fuel efficiency by producing a versatile syngas that can be u...  |  Gasification offers several primary benefits for upgrading solid feedstocks, particularly in terms of handling, environmental impact, and fuel efficiency. It converts difficult-to-handle solid feedstocks into a gaseous form that is easier to manage and use for various applications such as heating, cooking, transportati...  |  [ { "rubric_id": 1, "title": "Gaseous Conversion", "description": "Essential: Correctly identifies conversion of solid feedstocks to gaseous form for easier handling and application.", "weight": 4 }, { "rubric_id": 2, "title": "Impurity Removal", "description": "Essential: Accurately e...  |  
|  22  |  Carbon Reduction and Circular Utilization  |  What role does the air heater play in the steam-water circulation system?  |  The air heater in the steam-water circulation system preheats the air used for combustion, improving boiler efficiency and enhancing the overall thermal performance of the system.  |  The air heater is not part of the steam-water circulation system, but it is an important component in the steam generator system heat transfer and efficiency. The flue gas that exits from the steam generator is often as hot as and represents a major loss of heat and a source of inefficiency in the power plant. To addre...  |  [ { "rubric_id": 1, "title": "System Classification", "description": "Essential: Correctly identifies air heater as not part of steam-water circulation system.", "weight": 5 }, { "rubric_id": 2, "title": "Primary Function", "description": "Essential: Explains role in reducing flue gas ...  |  
|  23  |  Carbon Reduction and Circular Utilization  |  What is the primary function of a steam condenser?  |  The primary function of a steam condenser is to condense exhaust steam from a turbine back into water, creating a vacuum that increases the efficiency of the turbine and recycles the water for reuse in the system.  |  The primary function of a steam condenser is to condense the turbine exhaust steam using cooling water, creating a vacuum to reduce backpressure on the turbine and maximize plant efficiency, while also recovering and recycling quality feedwater back to the steam generation unit.  |  [ { "rubric_id": 1, "title": "Condensation Function", "description": "Essential: Correctly identifies the condenser's role in condensing turbine exhaust steam.", "weight": 4 }, { "rubric_id": 2, "title": "Cooling Water Use", "description": "Essential: Mentions the use of cooling water ...  |  
|  24  |  Carbon Reduction and Circular Utilization  |  What are the two main thermodynamic cycles used widely in power generation?  |  The two main thermodynamic cycles used widely in power generation are the Rankine cycle and the Brayton cycle.  |  The two thermodynamic cycles most widely used in power generation are the Rankine cycle and the Brayton cycle. In coal-fired power systems, the Rankine steam cycle is dominant, while the Brayton cycle is central to gas-turbine and combined-cycle applications.  |  [ { "rubric_id": 1, "title": "Correct Identification", "description": "Essential: Correctly identifies both Rankine and Brayton cycles as the primary thermodynamic cycles.", "weight": 5 }, { "rubric_id": 2, "title": "Cycle Description", "description": "Important: Briefly explains the f...  |  
|  25  |  Carbon Reduction and Circular Utilization  |  What are some key areas of ongoing research and development in improving steam turbines, particularly focusing on advancements in sealing technology and the creation of specialized measurement equipment for static strains and radial clearance in turbine components?  |  Key areas of ongoing research and development in improving steam turbines include: 1. **Advanced Sealing Technology**: - Development of **turbine labyrinth seals** with reduced leakage and improved efficiency. - Use of **brush seals** and **honeycomb seals** to minimize steam leakage while maintaining durability...  |  Improvement of the sealing technology for steam turbines is a continuing area of research and development. This becomes more important as the steam pressure is further increased. Also, the development of long-term measurement equipment for static strains in turbine components, as well as sensors for measuring the radia...  |  [ { "rubric_id": 1, "title": "Sealing Technology Advancements", "description": "Essential: Correctly identifies sealing technology as a key research area with emphasis on high-pressure steam applications.", "weight": 4 }, { "rubric_id": 2, "title": "Measurement Equipment Development", ...  |  
|  26  |  Carbon Reduction and Circular Utilization  |  What are the key technical challenges in oxy-fuel combustion technology, including oxygen concentration control, fuel–gas mixing, coal combustion behavior under different atmospheres, pollutant formation mechanisms, and safe oxygen handling in boiler systems?  |  The key technical challenges in oxy-fuel combustion technology include: 1. **Oxygen Concentration Control**: Maintaining precise oxygen levels in the combustion process is critical to ensure stable combustion and efficient energy conversion while minimizing the formation of undesirable byproducts. 2. **Fuel–Gas Mixin...  |  The key technical challenges in oxy-fuel combustion technology include: (1) Identifying the optimal oxygen concentration during combustion to balance high oxygen levels (which increase compressor demands) with low oxygen levels (which can lead to corrosive atmospheres and incomplete burnout). (2) Ensuring a homogeneous...  |  [ { "rubric_id": 1, "title": "Oxygen Concentration Balance", "description": "Essential: Correctly identifies the trade-off between high oxygen demand and corrosive/combustion inefficiency risks.", "weight": 4 }, { "rubric_id": 2, "title": "Fuel-Gas Homogeneity", "description": "Essenti...  |  
|  27  |  Carbon Reduction and Circular Utilization  |  During the combustion process, what substance is formed when sulfur in the fuel is oxidized?  |  Sulfur dioxide (SO₂)  |  When sulfur contained in coal or fuel oil is oxidized during combustion, it primarily forms sulfur dioxide (SO2). This product is important in boiler and power-plant engineering because it contributes to flue-gas sulfur emissions and acid-gas control requirements.  |  [ { "rubric_id": 1, "title": "Correct Product", "description": "Essential: Identifies sulfur dioxide (SO₂) as the correct oxidation product.", "weight": 5 }, { "rubric_id": 2, "title": "Oxidation Process", "description": "Essential: Explicitly states that oxidation occurs during combus...  |  
|  28  |  Carbon Reduction and Circular Utilization  |  What factors influence the effectiveness of sulfur capture in a bed reactor system involving limestone?  |  The effectiveness of sulfur capture in a bed reactor system involving limestone is influenced by factors such as temperature, particle size of limestone, calcination degree of limestone, gas flow rate, sulfur dioxide (SO₂) concentration, residence time, and the reactivity of the limestone.  |  The effectiveness of sulfur capture in a bed reactor system involving limestone is influenced by bed quality, including limestone distribution, mixing, and fluidization. Better contact between the limestone, sulfur dioxide, and oxygen increases sulfur capture. Additionally, increasing the fluidizing gas velocity decrea...  |  [ { "rubric_id": 1, "title": "Bed Quality", "description": "Essential: Correctly identifies bed quality (limestone distribution, mixing, fluidization) as a critical factor.", "weight": 4 }, { "rubric_id": 2, "title": "Limestone Contact", "description": "Essential: Explains the importan...  |  
|  29  |  Carbon Reduction and Circular Utilization  |  What process is necessary for the absorption of carbonyl sulfide (COS) during the washing step, and how does the choice between physical and COS hydrolysis steps depend on factors such as the type of wash used and economic considerations?  |  The process necessary for the absorption of carbonyl sulfide (COS) during the washing step is typically hydrolysis, which converts COS into hydrogen sulfide (H₂S) and carbon dioxide (CO₂), both of which can be more easily removed by the amine or other solvents used in the wash. The choice between physical absorption an...  |  The process necessary for the absorption of carbonyl sulfide (COS) during the washing step is either physical absorption or a COS hydrolysis step. The choice between these methods depends on the type of wash used and economic considerations. Chemical washes generally cannot absorb COS, requiring a COS hydrolysis step u...  |  [ { "rubric_id": 1, "title": "Process Coverage", "description": "Essential: Identifies physical absorption and COS hydrolysis as the two necessary processes.", "weight": 4 }, { "rubric_id": 2, "title": "Process Dependency", "description": "Essential: Explains the dependency on wash typ...  |  
|  30  |  Carbon Reduction and Circular Utilization  |  What methods are typically employed for sulfur recovery, and how does the handling of the tailgas from the Claus plant vary among different sulfur recovery processes?  |  Common methods for sulfur recovery include the Claus process, SCOT (Sulfur Recovery Tail gas) process, and other tail gas treatment technologies such as the Super Claus process, MDEA (Methyl Diethanolamine) process, and the Chiyoda-Clinsulf process. The handling of tailgas from the Claus plant varies depending on the p...  |  Sulfur recovery is generally achieved using Claus technology, although Polk is an exception in that it manufactures sulfuric acid rather than elemental sulfur. Differences in the Claus technology itself are generally only of a detailed nature. Considerable variety is shown in the handling of the tailgas from the Claus ...  |  [ { "rubric_id": 1, "title": "Claus Technology", "description": "Essential: Identifies Claus technology as the primary method for sulfur recovery.", "weight": 4 }, { "rubric_id": 2, "title": "Polk Exception", "description": "Essential: Notes Polk's use of sulfuric acid production inste...  |  
|  31  |  Carbon Reduction and Circular Utilization  |  What are some key benefits and limitations of Integrated Gasification Combined Cycle (IGCC) technology?  |  **Key Benefits of IGCC Technology:** 1. **Higher Efficiency**: IGCC plants can achieve higher thermal efficiency compared to conventional coal-fired power plants. 2. **Lower Emissions**: The gasification process allows for easier removal of pollutants (e.g., sulfur, mercury) before combustion, resulting in lower emiss...  |  Key benefits of Integrated Gasification Combined Cycle (IGCC) technology include higher system efficiency compared to conventional coal-fired power plants, reduced emissions of sulfur dioxide and nitrogen oxides due to the gasification process, and the potential for carbon capture and storage (CCS). Additionally, IGCC ...  |  [ { "rubric_id": 1, "title": "Efficiency Benefits", "description": "Essential: Correctly states IGCC has higher system efficiency than conventional coal plants.", "weight": 4 }, { "rubric_id": 2, "title": "Emission Impacts", "description": "Essential: Identifies reduced SO2 and NOx emi...  |  
|  32  |  Carbon Reduction and Circular Utilization  |  What are some key properties and limitations of glass fabrics used in high-temperature applications?  |  Key properties of glass fabrics in high-temperature applications include excellent thermal resistance (up to 500–600°C), good chemical resistance, electrical insulation, and mechanical strength at elevated temperatures. Limitations include brittleness, susceptibility to thermal shock, limited flexibility, and potential...  |  Glass fabrics offer outstanding performance in high-heat applications. In general, by using a proprietary finish they become resistant to acids, except by hydrofluoric and hot phosphoric acids in their most concentrated forms. They are attacked by strong alkalis at room temperature and weak alkalis at higher temperatur...  |  [ { "rubric_id": 1, "title": "Acid Resistance", "description": "Essential: Correctly identifies resistance to acids except hydrofluoric and hot phosphoric acids in concentrated forms.", "weight": 4 }, { "rubric_id": 2, "title": "Alkali Vulnerability", "description": "Essential: Accurat...  |  
|  33  |  Carbon Reduction and Circular Utilization  |  What are some key properties of Polyphenylene Sulfide (PPS) fibers, including their resistance to acids and alkalis, stability, flexibility, and filtration efficiency?  |  Polyphenylene Sulfide (PPS) fibers are known for their excellent chemical resistance to acids and alkalis, high thermal stability, good flexibility, and high filtration efficiency, making them suitable for harsh industrial and filtration applications.  |  Polyphenylene sulfide (PPS) fibers offer excellent resistance to acids, good-to-excellent resistance to alkalis, have excellent stability and flexibility, and provides excellent filtration efficiency. Maximum operating temperature is 220°C.  |  [ { "rubric_id": 1, "title": "Acid Resistance", "description": "Essential: Correctly states PPS fibers have excellent resistance to acids.", "weight": 4 }, { "rubric_id": 2, "title": "Alkali Resistance", "description": "Essential: Accurately describes good-to-excellent alkali resistanc...  |  
|  34  |  Carbon Reduction and Circular Utilization  |  What are some properties of polyester fabrics?  |  Polyester fabrics are durable, wrinkle-resistant, quick-drying, and retain their shape well. They are also resistant to shrinking and most chemicals, and they can be blended with other fibers to enhance their properties.  |  Polyester fabrics offer good resistance to most acids, oxidizing agents, and organic solvents. Concentrated sulfuric and nitric acids are the exception. Polyesters are dissolved by alkalis at high concentrations. Maximum operating temperature is .  |  [ { "rubric_id": 1, "title": "Chemical Resistance", "description": "Essential: Correctly identifies resistance to acids, oxidizing agents, and solvents.", "weight": 4 }, { "rubric_id": 2, "title": "Acid Exceptions", "description": "Essential: Mentions sulfuric and nitric acid exception...  |  
|  35  |  Carbon Reduction and Circular Utilization  |  What are some properties of polypropylene fabrics?  |  Polypropylene fabrics are lightweight, moisture-resistant, quick-drying, durable, and have good thermal insulation. They are also resistant to chemicals and mildew, and are often used in outdoor and performance apparel, as well as in geotextiles and medical applications.  |  Polypropylene fabrics offer good tensile strength and abrasion resistance. They perform well in organic and mineral acids, solvents, and alkalis. Polypropylene is attacked by nitric and chlorosulfonic acids, and sodium and potassium hydroxide at high temperatures and concentrations. Maximum operating temperature is 100...  |  [ { "rubric_id": 1, "title": "Tensile Strength", "description": "Essential: Correctly identifies good tensile strength as a key property.", "weight": 3 }, { "rubric_id": 2, "title": "Abrasion Resistance", "description": "Essential: Mentions abrasion resistance as a core characteristic....  |  
|  36  |  Carbon Reduction and Circular Utilization  |  What are ionic liquids?  |  Ionic liquids are salts that are in the liquid state at or near room temperature. They are composed entirely of ions, typically with a combination of organic cations and inorganic or organic anions, and have low melting points compared to other ionic compounds.  |  Ionic liquids are a broad category of salts, typically containing an organic cation and either an inorganic or organic anion. They are generally liquid at room temperature, nonvolatile, thermally stable, and nonflammable. Ionic liquids can dissolve gaseous and are stable at temperatures up to several hundred degrees Ce...  |  [ { "rubric_id": 1, "title": "Definition of Ionic Liquids", "description": "Essential: Correctly identifies ionic liquids as salts with organic cations and inorganic/organic anions.", "weight": 5 }, { "rubric_id": 2, "title": "Room Temperature Liquids", "description": "Essential: State...  |  
|  37  |  Others  |  What are the primary uses of traded coals worldwide?  |  The primary uses of traded coals worldwide are for electricity generation, steel production, and cement manufacturing.  |  The principal uses of traded coals worldwide are for electricity generation and steel manufacture, with other industrial users and domestic consumption making up the remainder.  |  [ { "rubric_id": 1, "title": "Electricity Generation", "description": "Essential: Correctly identifies electricity generation as a primary use of traded coal.", "weight": 4 }, { "rubric_id": 2, "title": "Steel Manufacture", "description": "Essential: Accurately states steel production ...  |  
|  38  |  Geology  |  What types of post-depositional effects can be observed in coal-bearing sequences and how do they typically manifest?  |  Post-depositional effects in coal-bearing sequences include compaction, oxidation, weathering, biodegradation, and metamorphism. These effects typically manifest as changes in coal rank, loss of volatile matter, alteration of maceral composition, fracturing, and the formation of secondary minerals.  |  Post-depositional effects in coal-bearing sequences include structural changes such as faults, joints (cleats), folds, and igneous associations, as well as mineral precipitation that alters the original form and bedding. These effects can range from gentle warping to complex thrusting and folding, often resulting in hi...  |  [ { "rubric_id": 1, "title": "Structural Changes", "description": "Essential: Identifies faults, joints (cleats), folds, and igneous associations as key post-depositional effects.", "weight": 4 }, { "rubric_id": 2, "title": "Mineral Precipitation", "description": "Essential: Mentions m...  |  
|  39  |  Geology  |  What types of coal and lignite deposits are found in different regions of Bosnia?  |  Bosnia and Herzegovina has several types of coal and lignite deposits, primarily found in the following regions: 1. **Lignite (Brown Coal):** - **Tuzla Coal Basin (Tuzla region):** Contains lignite deposits of the Upper Cretaceous and Paleocene age. - **Banja Luka region (Bijeljina and Prijedor):** Lignite depos...  |  Palaeogene–Neogene lignite intermontane basins are present in several areas of Bosnia. In the Sarajevo-Zenica area, subbituminous coal and lignite are present in large quantities. The coals have high moisture and ash contents. In the east of Bosnia, at Gacko, lignite seams are up to 10 m, and in the Ugljevic area the s...  |  [ { "rubric_id": 1, "title": "Region Identification", "description": "Essential: Correctly identifies Sarajevo-Zenica, Gacko, Ugljevic, Kongora, and Stanari as key regions.", "weight": 4 }, { "rubric_id": 2, "title": "Coal Type Accuracy", "description": "Essential: Specifies subbitumin...  |  
|  40  |  Geology  |  What significant coal deposits does the Czech Republic possess, including their geographical distribution and characteristics?  |  The Czech Republic possesses significant coal deposits, primarily lignite and hard coal. The main coal basins are: 1. **Lignite (Brown Coal):** - **North Bohemian Basin (Most Basin):** Located in northern Bohemia, this is the largest lignite-producing region. It includes the Děčín and Most areas. - **Central Boh...  |  The Czech Republic has numerous deposits of black and brown coals spread widely across the country. The chief black coalfield is that of Ostrava-Karvina on the north-eastern border, containing Upper Carboniferous strata that represent a continuation of the Upper Silesian Coalfield in Poland. The lower part of the seque...  |  [ { "rubric_id": 1, "title": "Coal Types", "description": "Essential: Identifies both black and brown coal deposits in the Czech Republic.", "weight": 4 }, { "rubric_id": 2, "title": "Ostrava Karvina Basin", "description": "Essential: Specifies the location and geological context of th...  |  
|  41  |  Geology  |  What types of coal are present in the Alps and Sardinia?  |  The types of coal present in the Alps and Sardinia are primarily **bituminous coal** and **anthracite**. These coals are found in sedimentary basins and are associated with the geological history of the region, including the Alpine orogeny.  |  Carboniferous coals are present in the structurally complex areas of the Alps and Sardinia. Palaeogene–Neogene lignites and subbituminous coals are found in the Apennines and Sardinia. The latter coalfield at Sulcis has subbituminous coal as a result of volcanic amelioration. Mining is on a very small scale.  |  [ { "rubric_id": 1, "title": "Carboniferous Coal Mention", "description": "Essential: Correctly identifies Carboniferous coals in structurally complex areas of Alps and Sardinia.", "weight": 5 }, { "rubric_id": 2, "title": "Palaeogene–Neogene Coals", "description": "Essential: Accurate...  |  
|  42  |  Geology  |  What are the key features of Kosovo's coal resources, including their geological age and mining locations?  |  Kosovo's coal resources are primarily of Tertiary geological age, with the majority found in the region of the Kosovo Coal Basin. Key features include: 1. **Geological Age**: Tertiary (mainly Paleogene). 2. **Mining Locations**: - **Leposavić Coal Basin** (also known as the Kosovo Coal Basin), located in northern ...  |  Kosovo has large lignite resources situated in three areas: the Kosovo, Dukagjin, and Drenica Basins. The coals are of Pliocene age, and seam average thickness is 3–5 meters; mining has concentrated in the Kosovo Basin, with the Sibovc mining area being targeted for future development.  |  [ { "rubric_id": 1, "title": "Basins Identified", "description": "Essential: Correctly lists all three basins (Kosovo, Dukagjin, Drenica).", "weight": 4 }, { "rubric_id": 2, "title": "Geological Age", "description": "Essential: Accurately states Pliocene age of the coals.", "weight...  |  
|  43  |  Geology  |  What are the key characteristics and locations of Poland's coal deposits?  |  Poland's coal deposits are primarily located in the Upper Silesian Basin in the south and the Lublin Basin in the east. The key characteristics include: - **Type of Coal**: Mostly bituminous coal, with some anthracite in Upper Silesia. - **Reserves**: Poland has the 10th largest coal reserves in Europe. - **Mining Met...  |  Poland's coal deposits are characterized by large reserves and a long-established coalmining industry. The key coalfields are: 1. **Upper Silesia**: Contains a thick sequence of upper Carboniferous sediments with 250 coal seams in the lower part and 60 in the upper part. The coal is high-volatile bituminous with low a...  |  [ { "rubric_id": 1, "title": "Coalfield Identification", "description": "Essential: Correctly lists all four key coalfields (Upper Silesia, Lower Silesia, Lublin, Lignite Basins).", "weight": 4 }, { "rubric_id": 2, "title": "Coal Type Classification", "description": "Essential: Accurat...  |  
|  44  |  Geology  |  What are the key characteristics and uses of the lignite reserves found in Oltenia, Romania?  |  Lignite reserves in Oltenia, Romania, are characterized by their low rank, high moisture content, and relatively low heat value. They are primarily used for electricity generation and heating. The region's lignite is mined in open-pit operations and plays a significant role in Romania's energy production, particularly ...  |  The key characteristics of the lignite reserves found in Oltenia, Romania, include their occurrence in Palaeogene–Neogene deposits, alignment in an east–west direction, and high ash and sulfur content. These reserves are primarily mined from thick seams using both opencast and underground methods. The main use of this ...  |  [ { "rubric_id": 1, "title": "Geological Age", "description": "Essential: Correctly identifies Palaeogene–Neogene deposits as the geological context of Oltenia lignite.", "weight": 4 }, { "rubric_id": 2, "title": "Geologic Orientation", "description": "Essential: States the east–west a...  |  
|  45  |  Geology  |  What types of coal deposits does Serbia possess, and where are they located?  |  Serbia possesses mainly two types of coal deposits: **lignite** and **bituminous coal**. - **Lignite** is the most abundant type and is primarily found in the **Kolubara Basin** (near Belgrade) and the **Kostolac Basin** (in the southeast of the country). - **Bituminous coal** is found in smaller quantities and is ma...  |  Serbia possesses two main types of coal deposits: black coal and brown coal (lignite). The black coal, of Palaeozoic (Carboniferous) and Mesozoic ages, is found in the structurally complex regions of the southeast part of the country. The brown coal (lignite) deposits, which are more extensive, are of Palaeogene–Neogen...  |  [ { "rubric_id": 1, "title": "Coal Types Identified", "description": "Essential: Correctly identifies both black coal and brown coal (lignite) as Serbia's main coal types.", "weight": 4 }, { "rubric_id": 2, "title": "Black Coal Age", "description": "Essential: Accurately states Palaeoz...  |  
|  46  |  Geology  |  What types of coal are found in the Mali–Niger Basin, and what are their typical thicknesses and moisture/ash content ranges?  |  The Mali–Niger Basin contains primarily lignite and sub-bituminous coal. Typical thicknesses of coal seams in the region range from 0.5 to 3 meters. The moisture content of these coals generally ranges from 20% to 40%, while the ash content typically ranges from 10% to 30%.  |  Upper Cretaceous and Palaeogene–Neogene brown coals are found in the Mali–Niger Basin. The seams typically reach thicknesses of up to 10 meters, with moisture values ranging from 30% to 50% and ash values ranging from 10% to 30%.  |  [ { "rubric_id": 1, "title": "Coal Type Accuracy", "description": "Essential: Correctly identifies Upper Cretaceous and Palaeogene–Neogene brown coals.", "weight": 4 }, { "rubric_id": 2, "title": "Thickness Range", "description": "Essential: States seams reach up to 10 meters in thickn...  |  
|  47  |  Geology  |  What geological formations cover the eastern half of Namibia and what types of deposits might be present there?  |  The eastern half of Namibia is primarily covered by the Kalahari Basin, which consists of unconsolidated sediments such as sand, silt, and clay. This region is part of the Kalahari Desert and contains alluvial and palaeochannel deposits, which may include gold, diamonds, and other alluvial minerals. Additionally, the a...  |  The eastern half of Namibia is covered by post-Karoo sediments of the Kalahari Group. It is possible that Karoo sediments underlie a portion of this area and may contain coals of similar aspect to those found in Botswana.  |  [ { "rubric_id": 1, "title": "Kalahari Group Mention", "description": "Essential: Correctly identifies Kalahari Group as the primary geological formation.", "weight": 4 }, { "rubric_id": 2, "title": "Post-Karoo Sediments", "description": "Essential: Specifies post-Karoo sedimentary con...  |  
|  48  |  Geology  |  What geological formations and characteristics can be observed in the Nigerian Coalfield?  |  The Nigerian Coalfield, primarily located in the Enugu and Kogi states, exhibits several geological formations and characteristics, including: 1. **Lower Grit Formation** – Composed mainly of sandstone and grit, this layer is the uppermost and is relatively thin. 2. **Coal Measures Formation** – This is the main coal...  |  Coal-bearing sediments of Cretaceous and Palaeogene–Neogene age overlie Precambrian basement in the south-eastern part of Nigeria. These sediments dip to the west, where they are overlain by floodplain deposits of the River Niger. The Nigerian Coalfield is divided into several mining areas: the Enugu, Ezimo, Orukpa, Ok...  |  [ { "rubric_id": 1, "title": "Geological Age", "description": "Essential: Correctly identifies Cretaceous and Palaeogene–Neogene coal-bearing sediments.", "weight": 4 }, { "rubric_id": 2, "title": "Basement Rock", "description": "Essential: Mentions Precambrian basement as underlying s...  |  
|  49  |  Geology  |  What are the characteristics of the coal deposits found in the Luangwa, Luano, and Maamba areas of Zambia?  |  The coal deposits in the Luangwa, Luano, and Maamba areas of Zambia are characterized by their high quality, with low sulfur and ash content, making them suitable for both domestic energy production and export. These deposits are primarily bituminous coal, found in the Karoo Supergroup sedimentary rocks, and are part o...  |  The coal deposits in the Luangwa, Luano, and Maamba areas of Zambia are characterized as follows: - **Luangwa**: The coals are high-volatile bituminous with high ash content and can be up to thick. - **Luano**: The coal seams are relatively thin, high-volatile bituminous, with high ash content; some coal has coking pr...  |  [ { "rubric_id": 1, "title": "Coal Type Accuracy", "description": "Essential: Correctly identifies high-volatile bituminous coal for all three regions.", "weight": 4 }, { "rubric_id": 2, "title": "Ash Content Mention", "description": "Essential: Notes high ash content as a shared chara...  |  
|  50  |  Geology  |  What specific types of coal are found in the Wankie and Lubimbi coalfields of Zimbabwe's Karoo sequence, and what are their characteristics?  |  The Wankie and Lubimbi coalfields in Zimbabwe's Karoo sequence primarily contain **bituminous coal** and **sub-bituminous coal**. These coals are characterized by: - **Bituminous coal**: High carbon content (around 60–80%), moderate to high calorific value, and used mainly for electricity generation and steel producti...  |  The specific types of coal found in the Wankie and Lubimbi coalfields of Zimbabwe's Karoo sequence are medium- to high-volatile bituminous coals. These include a lower coking coal and an upper steam coal, both generally characterized by low sulfur contents.  |  [ { "rubric_id": 1, "title": "Coal Type Identification", "description": "Essential: Correctly identifies medium- to high-volatile bituminous coals as the primary type in Wankie and Lubimbi.", "weight": 4 }, { "rubric_id": 2, "title": "Coking Coal Mention", "description": "Important: Sp...  |  
|  51  |  Geology  |  What specific characteristics do the Mesozoic (Jurassic) black coals found in the northern mountainous regions of Takhar and Badakhshan have?  |  The Mesozoic (Jurassic) black coals found in the northern mountainous regions of Takhar and Badakhshan are characterized by high carbon content, low ash and sulfur content, and a bituminous to sub-bituminous rank. They are typically associated with sedimentary basins formed in a marine to coastal swamp environment and ...  |  Mesozoic (Jurassic) black coals found in the northern mountainous regions of Takhar and Badakhshan are relatively undisturbed, with seams up to in thickness. The coal is bituminous with low ash and sulfur contents and has coking properties.  |  [ { "rubric_id": 1, "title": "Bituminous Type", "description": "Essential: Correctly identifies the coal as bituminous.", "weight": 4 }, { "rubric_id": 2, "title": "Low Ash Content", "description": "Essential: States the coal has low ash content.", "weight": 3 }, { "rubric_...  |  
|  52  |  Geology  |  What types of coal are known from Bolivia?  |  Bolivia is known for having **anthracite** and **bituminous coal** deposits.  |  Two types of coal are known from Bolivia: anthracite of Permian age and lignites of Palaeogene–Neogene age. Anthracite is located on the Copacabana Peninsula and on the Isla del Sol, Lake Titicaca. Seams are in the form of coal lenses or very thin beds of anthracite with low sulfur content. The Palaeogene–Neogene ligni...  |  [ { "rubric_id": 1, "title": "Coal Types Identified", "description": "Essential: Correctly names anthracite and lignites as Bolivia's coal types.", "weight": 4 }, { "rubric_id": 2, "title": "Geological Ages Specified", "description": "Essential: Accurately states Permian for anthracite...  |  
|  53  |  Geology  |  What types of coal are found in the Karaganda Basin and what characteristics do they possess?  |  The Karaganda Basin in Kazakhstan contains primarily bituminous and sub-bituminous coals. These coals are characterized by high calorific value, moderate to high volatile matter content, and relatively low sulfur content. They are also known for their coking properties, making them suitable for use in the metallurgical...  |  The Karaganda Basin in Kazakhstan contains bituminous coal, ranging from high-volatile bituminous to anthracite. These coals have high ash and medium sulfur contents, with the lower seams possessing good coking properties. The basin features a thick sequence of Carboniferous sediments with numerous coal seams of varyin...  |  [ { "rubric_id": 1, "title": "Coal Types Identified", "description": "Essential: Correctly identifies bituminous and anthracite as primary coal types in Karaganda Basin.", "weight": 4 }, { "rubric_id": 2, "title": "Volatility Range", "description": "Important: Specifies high-volatile b...  |  
|  54  |  Geology  |  What significant coal deposits does Tajikistan possess and how are they being exploited?  |  Tajikistan possesses significant coal deposits, primarily located in the Khatlon region, particularly in the districts of Vose and Kurgan-Tyube. The country's coal reserves are estimated at around 1.2 billion tons, with anthracite and bituminous coal being the main types. These deposits are being exploited through both...  |  Tajikistan has important coal deposits at Shurob and Fon-Yaghnob and is beginning to exploit the bituminous coals of East Zidi by open-pit methods and the anthracite coal at Nazarailok by underground mining.  |  [ { "rubric_id": 1, "title": "Shurob and Fon-Yaghnob deposits", "description": "Essential: Correctly identifies Shurob and Fon-Yaghnob as major coal deposits in Tajikistan.", "weight": 4 }, { "rubric_id": 2, "title": "East Zidi bituminous coal", "description": "Essential: Mentions bitu...  |  
|  55  |  Geology  |  Where are the Malaysian coals located?  |  The Malaysian coals are primarily located in the states of **Sarawak** and **Sabah** on the island of Borneo. Major coal deposits are found in areas such as **Limbang**, **Sarikei**, and **Sibu** in Sarawak.  |  Malaysian coals are found on the west coast of the West Malaysian peninsula and on the East Malaysian side of the island of Borneo in the states of Sabah and Sarawak. In Sabah, subbituminous coals with some coking properties but often high sulfur contents have been mined at Silimpopon. In Sarawak, higher quality bitumi...  |  [ { "rubric_id": 1, "title": "Essential Locations", "description": "Essential: Correctly identifies West Malaysia, Sabah, and Sarawak as primary coal regions.", "weight": 4 }, { "rubric_id": 2, "title": "Geographic Specificity", "description": "Important: Specifies coastal locations (w...  |  
|  56  |  Geology  |  What types of coal are found in the Taiwan coalfields?  |  The main types of coal found in the Taiwan coalfields are bituminous coal and anthracite.  |  The Taiwan coalfields contain high-volatile bituminous, low-volatile bituminous, subbituminous, and semi-anthracite coals. Identifying these ranks is important because coal rank influences calorific value, volatile matter, combustion behavior, and utilization potential.  |  [ { "rubric_id": 1, "title": "High-Volatile Bituminous", "description": "Essential: Correctly identifies high-volatile bituminous coal as a type in Taiwan coalfields.", "weight": 4 }, { "rubric_id": 2, "title": "Subbituminous Coverage", "description": "Essential: Correctly identifies s...  |  
|  57  |  Geology  |  What are the key characteristics and locations of New Zealand's coal resources?  |  New Zealand's coal resources are primarily characterized by their high quality, with a significant portion being metallurgical (coking) coal suitable for steel production. The key coal basins are located in the South Island, particularly in the West Coast region, including the Buller and Waikato areas. These deposits a...  |  New Zealand's coal resources are primarily Cretaceous–Palaeogene–Neogene in age, with the exception of a few thin Jurassic coals. Key locations include the western part of the North Island and the north-western and south-eastern districts of the South Island. The Waikato Coal region in the North Island contains the maj...  |  [ { "rubric_id": 1, "title": "Age Classification", "description": "Essential: Correctly identifies Cretaceous–Palaeogene–Neogene age with Jurassic exception.", "weight": 4 }, { "rubric_id": 2, "title": "Key Locations", "description": "Essential: Mentions North Island western regions an...  |  
|  58  |  Geology  |  What are sapropelic coals?  |  Sapropelic coals are a type of coal formed from the remains of aquatic plants and algae that accumulated in swampy or lake environments. They are characterized by high hydrogen and oxygen content, low carbon content, and a high moisture level compared to other coal types.  |  Sapropelic coals are formed from the biological and physical degradation products of coal peat-forming environments, with the addition of other materials such as plant spores and algae. The resultant sediment is an accumulation of colloidal organic mud in which concentrations of spore remains and/or algae are present. ...  |  [ { "rubric_id": 1, "title": "Essential Definition", "description": "Essential: Correctly defines sapropelic coals as formed from degradation products of peat-forming environments with spores and algae.", "weight": 4 }, { "rubric_id": 2, "title": "Formation Process", "description": "Es...  |  
|  59  |  Geology  |  What is the Abrasion Index and how is it determined for coal samples?  |  The Abrasion Index is a measure of the tendency of coal to produce dust during handling and transportation. It is determined by the amount of coal fines (dust) generated when a coal sample is subjected to mechanical abrasion in a standardized test apparatus, typically the Los Angeles Abrasion Machine. The test involves...  |  The Abrasion Index is a measure of the abrasive effect of coal on machinery, determined by the loss in mass of metal blades in a mill after processing a coal sample, expressed as milligrams of metal per kilogram of coal.  |  [ { "rubric_id": 1, "title": "Definition Accuracy", "description": "Essential: Correctly defines Abrasion Index as a measure of coal's abrasive effect on machinery.", "weight": 4 }, { "rubric_id": 2, "title": "Method Description", "description": "Essential: Accurately describes the mas...  |  
|  60  |  Geology  |  What are the limitations of using grab samples for obtaining coal for analysis?  |  Grab samples for coal analysis have several limitations, including: 1. **Inhomogeneity**: Coal is a heterogeneous material, and a single grab sample may not represent the entire batch or lot. 2. **Sampling Bias**: The sample may be taken from a non-representative portion of the coal, leading to inaccurate results. 3...  |  The limitations of using grab samples for obtaining coal for analysis include the lack of controls to ensure the coal is representative, which can easily lead to a bias in selection, such as favoring bright coal sections. However, grab samples can still be used for determining vitrinite reflectance measurements as an i...  |  [ { "rubric_id": 1, "title": "Representativeness Coverage", "description": "Essential: Identifies lack of controls ensuring coal sample representativeness.", "weight": 4 }, { "rubric_id": 2, "title": "Selection Bias", "description": "Essential: Mentions bias toward bright coal sections...  |  
|  61  |  Geology  |  What does Solid Core Recovery represent?  |  Solid Core Recovery represents the percentage of the original core length that is successfully recovered in an undisturbed or minimally disturbed state during drilling operations, typically in geological or geotechnical investigations.  |  Solid Core Recovery represents the total length of pieces of core recovered that have a full diameter, expressed as a percentage of the full core run.  |  [ { "rubric_id": 1, "title": "Core Definition", "description": "Essential: Accurately defines Solid Core Recovery as the total length of full-diameter core pieces.", "weight": 4 }, { "rubric_id": 2, "title": "Percentage Context", "description": "Essential: Correctly states it is expres...  |  
|  62  |  Geology  |  What are the definitions of coal reserves, including their types: probable coal reserve and proved coal reserve?  |  **Coal Reserves** are coal resources that can be economically extracted or produced using current technology and under current economic conditions. - **Proved Coal Reserve**: Coal that can be mined with a high degree of certainty, based on detailed geological and engineering studies, and is economically recoverable un...  |  (i) A coal reserve is the economically mineable part of a measured and/or indicated resource. It includes diluting materials and allowances for mining losses defined by studies at pre-feasibility or feasibility level that demonstrate coalmining can be justified. (ii) A probable coal reserve is the economically mineable...  |  [ { "rubric_id": 1, "title": "Essential Definition", "description": "Essential: Accurately defines coal reserves as the economically mineable part of measured/indicated resources.", "weight": 5 }, { "rubric_id": 2, "title": "Reserve Types", "description": "Essential: Distinguishes betw...  |  
|  63  |  Geology  |  What specific physical properties do coal-bearing sequences exhibit when compared to other common lithologies found within them?  |  Coal-bearing sequences typically exhibit lower density, lower seismic velocity, and higher organic content compared to surrounding lithologies such as sandstone, shale, and limestone. They also show distinct electromagnetic properties and are often characterized by higher porosity and permeability in the surrounding ro...  |  Coal as a lithology responds well to most geophysical methods, in that its physical properties contrast with those of other lithologies commonly found in coal-bearing sequences. Coal has, in general, a lower density, a lower seismic velocity, a lower magnetic susceptibility, a higher electrical resistivity, and low rad...  |  [ { "rubric_id": 1, "title": "Density Contrast", "description": "Essential: Identifies coal's lower density compared to surrounding lithologies.", "weight": 3 }, { "rubric_id": 2, "title": "Seismic Velocity", "description": "Essential: States coal's lower seismic velocity relative to o...  |  
End of preview. Expand in Data Studio⟨41⟩
* * *
  *  Previous⟨29⟩
  * 1⟨42⟩
  * 2⟨43⟩
  * 3⟨44⟩
  * ...⟨45⟩
  * 8⟨46⟩
  * Next ⟨43⟩


  * Languages⟨47⟩
  * Directory Layout⟨48⟩


#   ⟨49⟩ CoalBench: A Bilingual Coal-Domain Dataset Suite for LLM Post-Training 
This folder contains the CoalBench release package: bilingual coal-mining datasets, prompt templates, post-training/evaluation code, and the main post-training learning curves exported from SwanLab.
##   ⟨47⟩ Languages 
  * EN: English
  * ZH: Chinese


##   ⟨48⟩ Directory Layout 
CoalBench/ CoalBench/ Final dataset files for full data, SFT, DPO, and RaR training.
Code/ Data construction, post-training, evaluation, plotting, and reward code.
Prompt/ Prompt templates used for answer generation, rubric generation, and GPT-as-judge evaluation.
Post-training results/ SwanLab CSV exports and rendered learning-curve figures.
  1. Dataset Files


* * *
All dataset files are JSON arrays. Each record is indexed by "id" and includes a coal-domain "class" label and "question". The derived training formats keep the same sample order and identifiers as the corresponding full dataset.
1.1 Full CoalBench Files

```
Files:
- CoalBench/CoalBench-EN.json
- CoalBench/CoalBench-ZH.json

Schema:
{
  "id": int,
  "class": str,
  "question": str,
  "answer1": str,
  "answer2": str,
  "rubrics": [rubric]
}

Description:
- answer1 is generated from the question only.
- answer2 is generated from the question plus weak supervision from the class
  label and reference answer.
- rubrics are structured evaluation criteria generated from the question and
  reference-guided answer.

1.2 Supervised Fine-Tuning Files

```

Files:
  * CoalBench/CoalBench-SFT-EN.json
  * CoalBench/CoalBench-SFT-ZH.json


Schema: { "id": int, "class": str, "question": str, "answer": str }
Description: Question-answer pairs for supervised fine-tuning. The "answer" field is derived from answer2 in the full dataset.
1.3 Direct Preference Optimization Files

```
Files:
- CoalBench/CoalBench-DPO-EN.json
- CoalBench/CoalBench-DPO-ZH.json

Schema:
{
  "id": int,
  "class": str,
  "question": str,
  "chosen": str,
  "rejected": str
}

Description:
Preference pairs for DPO. "chosen" corresponds to answer2 and "rejected"
corresponds to answer1.

1.4 Rubric-as-Reward Files
~~~~~~~~~~~~~~~~~~~~~~~~~~
Files:
- CoalBench/CoalBench-RaR-EN.json
- CoalBench/CoalBench-RaR-ZH.json

Schema:
{
  "id": int,
  "class": str,
  "question": str,
  "rubrics": [rubric]
}

Description:
Rubric-as-Reward (RaR) data for reward-model-free reinforcement learning. Each
question is paired with a set of structured rubrics adapted from the HealthBench
rubric style.


2. Rubric Format
----------------
Each rubric item has the following schema:

{
  "rubric_id": int,
  "title": str,
  "description": str,
  "weight": int
}

Rubric categories are encoded at the beginning of "description":
- Essential: critical facts or conclusions required for a valid answer.
  Typical positive weight: 3 to 5.
- Important: key reasoning steps, technical details, or completeness criteria.
  Typical positive weight: 2 to 3.
- Optional: additional detail, clarity, or explanatory depth.
  Typical positive weight: 1 to 2.
- Pitfall: common misconceptions, unsafe guidance, or missing assumptions.
  Typical negative weight: -1 to -2.


3. Dataset Statistics
---------------------
Statistics computed from the JSON files in CoalBench/:

English subset:
- Full file: CoalBench-EN.json
- Instances: 742
- Classes: 26
- Total rubrics: 8,387
- Average rubrics per instance: 11.30

Chinese subset:
- Full file: CoalBench-ZH.json
- Instances: 526
- Classes: 17
- Total rubrics: 8,240
- Average rubrics per instance: 15.67


4. Prompt Files
---------------
Files in Prompt/ document the main prompt templates used in the pipeline:

- Question only.txt
  Generates answer1 from the question alone.

- Question with reference.txt
  Generates answer2 from the question, class label, and reference answer.

- PromptHealthBenchEn.txt
  English rubric-generation prompt adapted from the HealthBench rubric style.

- PromptHealthBenchCn.txt
  Chinese rubric-generation prompt adapted from the same rubric style.

- GPT-as-judge.txt
  Integer 1-10 answer-quality judging prompt using question, reference answer,
  and model answer as inputs.

Note: some prompt/code files may display mojibake if opened with a mismatched
encoding. Use UTF-8 where possible.


5. Code Files
-------------
Files in Code/ are research scripts rather than a single packaged command-line
tool. Paths and device settings are environment-specific and should be updated
before rerunning.

- runEn.py
  English data construction pipeline using Qwen3-32B. Stages include input
  cleaning/reindexing, question-only answer generation, reference-guided answer
  generation, rubric generation, empty-rubric repair, final filtering/reindexing,
  and class mismatch processing.

- runCn.py
  Chinese data construction pipeline using Qwen3-32B. Stages include source
  conversion, answer generation, rubric generation, rubric repair, and final
  dataset construction.

- runQwen2.5_0.5B.py
  Post-training and evaluation script for Qwen2.5-0.5B-Instruct with ms-swift.
  It includes stages for:
  - SFT LoRA training, inference, BLEU-1/ROUGE-L evaluation, and plotting.
  - DPO LoRA training, inference, GPT-as-judge scoring, and plotting.
  - RaR/GRPO LoRA training with rubric reward, inference, reward comparison,
    and plotting.
  - SwanLab CSV learning-curve plotting.
  - Dataset validation and class/rubric distribution analysis.

- rubric_Reward2.py
  External ms-swift ORM reward function for RaR/GRPO. It embeds model responses
  and rubric text with BAAI/bge-m3, computes cosine similarity, applies a
  floor-scaled continuous reward, adds positive rubric weights, and subtracts
  matching pitfall weights.


6. Post-Training Results
------------------------
Post-training results/ contains SwanLab exports and rendered figures:

CSV files:
- coalbench-sft-lora-2026-6-25_15_29_18.csv
  SFT training and evaluation loss over training steps.

- coalbench-dpo-2026-6-25_15_29_08.csv
  DPO chosen/rejected rewards for training and evaluation, plus reward margins.

- coalbench-grpo-rubric-lora-2026-6-25_15_28_14.csv
  RaR/GRPO rubric reward curves for training and evaluation.

- coalbench-grpo-rubric-lora-2026-6-25_15_29_00.csv
  RaR/GRPO KL curves for training and evaluation.

Figures:
- Post-training results/figures/SwanLabSFT.png
- Post-training results/figures/SwanLabDPO.png
- Post-training results/figures/SwanLabRaR.png

These figures are generated from the CSV files by Stage 4 of
Code/runQwen2.5_0.5B.py.


7. Reproducibility Notes
------------------------
- The scripts assume local model paths such as Qwen3-32B, Qwen2.5-0.5B-Instruct,
  and BAAI/bge-m3. Update these paths for a new environment.
- The scripts use Huawei Ascend device environment variables in their current
  form. Adjust device settings for CUDA, CPU, or other accelerators.
- The post-training script depends on ms-swift, PyTorch, pandas, NumPy,
  matplotlib, and related evaluation utilities.
- SwanLab logging is enabled in the training commands; configure or disable it
  as needed.
- The released dataset files in CoalBench/ are the primary artifacts. The code
  records the construction and evaluation workflow used to produce and analyze
  them.

```

Copy to bucket new
Use this dataset 

Downloads last month
    109
Number of rows: 5,072 Total file size: 12.3 MB
System theme
Company
TOS⟨50⟩ Privacy⟨51⟩ About⟨52⟩ Careers⟨53⟩ ⟨1⟩
Website
Models⟨2⟩ Datasets⟨3⟩ Spaces⟨4⟩ Pricing⟨8⟩ Docs⟨6⟩
