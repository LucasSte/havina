from havina.graph_generator import GraphGenerator

# TODO:
# 1. Why who and which are not resolved? No, but the algorithm is smart enough to handle this case
# 3. Allow only substantives in relation? Yes
text = ("Stanford University was founded in 1885 by Leland Stanford—a railroad magnate who served as the eighth "
        "governor of and then-incumbent senator from California—and his wife, Jane, in memory of their only child, "
        "Leland Stanford Jr., who had died of typhoid fever aged 15 the previous year. The university admitted its "
        "first students on October 1, 1891, as a coeducational and non-denominational institution. Stanford "
        "University struggled financially after Leland's death in 1893 and again after much of the campus was"
        " damaged by the 1906 San Francisco earthquake. Following World War II, Frederick Terman, the university's "
        "provost, inspired and supported faculty and graduates entrepreneurialism to build a self-sufficient local "
        "industry, which would later be known as Silicon Valley")
generator = GraphGenerator(device='mps', forward_relations=True, link_entity=False, top_k=6, contiguous_token=True,
                           relation_length=4, threshold=0.04)

relations = generator(text, 4)  # 36, 62, 61

for item in relations:
    print(f"{item.head.text} ------ {item.tail.text}")
    for rel in item.relations:
        print(rel)
