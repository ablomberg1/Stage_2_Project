def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
<div class="concept">
    <div class="concept-title">
        ''' + concept_title
    html_text_2 = '''
    </div>
    <div class="concept-description">
        ''' + concept_description
    html_text_3 = '''
    </div>
</div>'''
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def make_HTML(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    return generate_concept_HTML(concept_title, concept_description)

EXAMPLE_LIST_OF_CONCEPTS = [ ["Structured Data", "<p>Structured data is organized in a fixed field. A string or list is structured data. Strings are a sequence of variables like a name or word.  A list is a sequence of anything, letters, words, numbers or characters.  Lists are more powerful than strings.</p>"],
                             ["Mutation and Aliases", "<p>Lists are mutable meaning they may be changed after being created. The string is not modified it actually changes the value of the string by creating a new string.  One thing to be cautious of is other variables that refer to that object. Alisases have 2 different ways to refer to the same object. The example provided in class was James Bond is also known as '007'.  Whatever happens to that person refered to as James Bond also happens to '007', the agent is the spy.</p>"],
                             ["Append and '+'", "<p>Append is a method, like a procedure, used similarly to the way we use find.  The object is appended or added to the list.  '+' is similar to concatenation, adding the lists together to create one list</p>"],
                             ["For Loop", "<p>Loops are a collection of things.  The for loop is a simpler way to cycle thru all the elements in a list than to use a while loop with len.  It is used when you have a section of code you want to repeat n number of times.</p>"],
                             ["Index and In", "<p>Index is a built in procedure that returns the first positon where the value is found in the list, but will not provide a -1 if the value is not found.  The procedure will result in an error.  In is another way to find a value within a list. If the value is in the list, output is True, otherwise the output is False.</p>"]]


def make_HTML_for_many_concepts(list_of_concepts):
    HTML = ""

    for concept in list_of_concepts:
        concept_HTML = make_HTML(concept)
        HTML = HTML + concept_HTML
    return HTML

print make_HTML_for_many_concepts(EXAMPLE_LIST_OF_CONCEPTS)
