from devduck.apps.blog.models import ProgLanguage, Subjects, Module, Course

# Create date for models ProgLanguage

list_prog_language = [
    'Java',
    'C',
    'C++',
    'C#',
    'JavaScript',
    'PHP',
    'Ruby',
    'R',
    'Go',
    'Swift',
    'Kotlin',
    'TypeScript',
    'Scala',
    'Rust',
    'Dart',
    'Elixir',
    'Matlab',
    'SQL',
]

for prog_language in list_prog_language:
    prog_language_obj = ProgLanguage(description=prog_language)
    prog_language_obj.save()


# Create date for models Subjects

list_subjects = [
    'Matemática Computacional',
    'Atividades Linguísticas',
    'Inglês Técnico',
    'Algoritmos e Programação',
    'Introdução a Computação',

    'Metodologia Científica',
    'Programação Orientada a Objetos',
    'Banco de Dados I',
    'Engenharia de Software I',
    'Estrutura de Dados I',
    'Estátisca',

    'Banco de Dados II',
    'Arquitetura de Computadores',
    'Sistemas Operacionais',
    'Estrutura de Dados II',
    'Programação para Internet I',
    'Engenharia de Software II',
    'Projeto Integrador I',

    'Engenharia de Software III',
    'Redes de Computadores',
    'Analise e Projeto de Sistemas',
    'Introdução a Administração',
    'Programação para Internet II',
    'Projeto Integrador II',

    'Interação Humano Computador',
    'Tópicos Especiais em Programação',
    'Programação para Dispositivos Móveis',
    'Engenharia de Software IV',
    'Projeto Integrador III',
    'Elaboração de Projetos de Pesquisa',

    'Segurança da Informação',
    'Empreendedorismo e Inovação',
    'Tópicos Especiais em Sistema de Informação',
    'Lesgislação Aplciada a Tecnologia da Informação',
    'Ética e Responsabilidade Socioambiental',
    'Trabalho de Conclusão de Curso',
]

for subject in list_subjects:
    subject_obj = Subjects(description=subject)
    subject_obj.save()

# Create date for models Module

list_module = [
    'Módulo I',
    'Módulo II',
    'Módulo III',
    'Módulo IV',
    'Módulo V',
    'Módulo VI',
]

for module in list_module:
    module_obj = Module(description=module, id_course=Course.objects.get(id=1))
    module_obj.save()