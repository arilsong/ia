try:
    from pyswip import Prolog
except ImportError as e:
    print(f"Erro ao importar pyswip: {e}")


def load_knowledge_base(prolog):
    prolog.consult("escola.pl")

def process_query(prolog, query):
    query = query.lower()

    try:
        if "todos os alunos" in query:
            result = list(prolog.query("todos_alunos(Alunos)"))
            result = result[0]['Alunos']
            alunos = ", ".join(result)
            return f"Alunos cadastrados: {alunos if result else 'Nenhum'}"

        elif "todas as disciplinas" in query:
            result = list(prolog.query("todas_disciplina(Disciplinas)"))
            result = result[0]['Disciplinas']
            disciplinas = ", ".join(result)
            return f"As disciplinas disponivel: {disciplinas if result else 'Nenhum'}"

        elif "média de notas" in query:
            aluno = query.split("média de notas de")[1].strip()
            print(aluno)
            if not aluno:
                return "Insira o numero do aluno(a) que deseja saber a media"
            result = list(prolog.query(f"media_notas(id_aluno({aluno}), Media)"))
            return f"Média de notas de {aluno}: {result[0]['Media'] if result else 'Não encontrado'}"

        elif "alunos acima da média" in query:
            result = list(prolog.query("alunos_acima_media(Alunos)"))
            result = result[0]['Alunos']
            alunos = ", ".join(result)
            return f"Alunos acima da média: {alunos if result else 'Nenhum'}"

        elif "disciplinas sem alunos" in query:
            result = list(prolog.query("disciplinas_sem_alunos(Disciplinas)"))
            result = result[0]['Disciplinas']
            disciplinas = ", ".join(result)
            return f"Disciplinas sem alunos: {disciplinas if result else 'Nenhuma'}"

        elif "professores da disciplina" in query:
            disciplina = query.split("professores da disciplina de")[1].strip()
            if not disciplina:
                return "Insira o numero da disciplina."
            disciplina = disciplina.upper()
            result = list(prolog.query(f"professores_disciplina(cod_disciplina('{disciplina}'), Professores)"))
            result = result[0]['Professores']
            professores = ", ".join(result)
            return f"Professores de {disciplina}: {professores if result else 'Não encontrado'}"

        elif "alunos reprovados" in query:
            result = list(prolog.query("alunos_reprovados(Reprovados)"))
            result = result[0]['Reprovados']
            reprovados = ", ".join(result)
            return f"{'Alunos reprovados: ' + reprovados if result else 'Nenhum aluno repovado no momento'}"

        elif "desciplina com mais alunos" in query:
            result = list(prolog.query("disciplinas_mais_alunos(Ranking)"))
            result = result[0]['Ranking']
            disciplina = ", ".join(result)
            return f"{'Disciplina com mais Alunos : ' + result if result else 'Nenhum aluno repovado no momento'}"

        elif "professores mais experientes" in query:
            result = list(prolog.query("professores_mais_experientes(Professores)"))
            result = result[0]['Professores']
            professores = ", ".join(result)
            return f"{'Disciplina com mais Alunos : ' + professores if result else 'Nenhum aluno repovado no momento'}"

        else:
            return "Pergunta não compreendida. Tente novamente."

    except Exception as e:
        print(f"Erro ao processar consulta: {str(e)}")
        return f"Ocorreu um erro por favor tente mais tarde"

def interact(user_input):
    prolog = Prolog()
    load_knowledge_base(prolog)

    response = process_query(prolog, user_input)
    return response

