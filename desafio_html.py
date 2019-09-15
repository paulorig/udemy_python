#!~/anaconda3/bin/python


def tag(tag, *args, **kwargs):
    atrs = ''
    for k, w in kwargs.items():
        atrs += f' {k.split("_")[-1]}="{w}"'
    return f'<{tag}{atrs}>{args}<{tag}>'

# <p class="alert"><span >Curso de Python 3, por </span><strong id="jf">Juracy Filho</strong><span > e </span><strong
# id="ll">Leonardo Leitão</strong><span >.</span></p>


if __name__ == "__main__":
    html_code =\
        tag('p',
            tag('span', 'Curso de Python 3, por '),
            tag('strong', 'Juracy Filho', id='jf'),
            tag('span', ' e '),
            tag('strong', 'Leonardo Leitão', id='ll'),
            tag('span', '.'),
            html_class='alert')
    print(html_code)
