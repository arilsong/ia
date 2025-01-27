%dados de alunos
aluno(id_aluno(11506), 'Nadine Delgado', data(15,03,2000), 'Praia, Palmarejo', 'nadine@gmail.com').
aluno(id_aluno(11625), 'Erica Almeida', data(22,11,2001), 'Praia, Palmarejo', 'erica@gmail.com').
aluno(id_aluno(11901), 'Arilson Gomes', data(10,07,2002), 'Praia, Palmarejo', 'arilson@gmail.com').
aluno(id_aluno(11945), 'Wilker Carvalho', data(10,07,2002), 'Praia, Palmarejo', 'wilker@gmail.com').

% dados de professores
professor(id_professor(1), 'Juvenal Perreira', 'Mestrado', 'Praia, Palmarejo', 'juvenal@gmail.com').
professor(id_professor(2), 'Constantino Garcia', 'Mestrado', 'Praia, Palmarejo', 'garcia@gmail.com').
professor(id_professor(3), 'Nelson beckam', 'Licenciado', 'Praia, Palmarejo', 'nelson@gmail.com').
professor(id_professor(4), 'Jair Delgado', 'Mestrado', 'Praia, Palmarejo', 'jair@gmail.com').

% dados de disciplinas
disciplina(cod_disciplina('INF017'), 'Inteligência Artificial', 60).
disciplina(cod_disciplina('INF036'), 'Programação por objectos', 45).
disciplina(cod_disciplina('INF012'), 'Sistemas de Informação', 50).
disciplina(cod_disciplina('INF057'), 'Administração de SO', 60).

% matriculas
matriculado(id_aluno(11504), cod_disciplina('INF017'), nota(14)).
matriculado(id_aluno(11504), cod_disciplina('INF012'), nota(12)).
matriculado(id_aluno(11625), cod_disciplina('INF017'), nota(16)).
matriculado(id_aluno(11901), cod_disciplina('INF057'), nota(2)).
matriculado(id_aluno(11945), cod_disciplina('INF012'), nota(5)).
matriculado(id_aluno(11945), cod_disciplina('INF017'), nota(16)).


% leciona disciplina
leciona(id_professor(1), cod_disciplina('INF017')).
leciona(id_professor(2), cod_disciplina('INF057')).
leciona(id_professor(3), cod_disciplina('INF036')).
leciona(id_professor(4), cod_disciplina('INF012')).

% regra para listar todos os alunos matriculados
todos_alunos(Alunos) :- findall(Nome, aluno(_, Nome, _, _, _), Alunos).

%regra para listar todas as diciplinas
todas_disciplina(Disciplinas):-findall(Nome, disciplina(_,Nome,_), Disciplinas).

% regra calcular media de notas de um aluno
media_notas(IdAluno, Media) :-
    findall(Nota, (matriculado(IdAluno, _, nota(Nota))), Notas),
    Notas \= [],
    sum_list(Notas, Total),
    length(Notas, Quantidade),
    Media is Total / Quantidade.

% regra para identificar alunos acima da media geral
alunos_acima_media(Alunos) :-
    findall(Media, media_notas(_, Media), TodasMedias),
    sum_list(TodasMedias, Total),
    length(TodasMedias, Quantidade),
    MediaGeral is Total / Quantidade,
    findall(Nome, (
        aluno(IdAluno, Nome, _, _, _),
        media_notas(IdAluno, MediaAluno),
        MediaAluno > MediaGeral
    ), Alunos).

% regra pra Disciplinas sem alunos
disciplinas_sem_alunos(Disciplinas) :-
    findall(Nome, (
        disciplina(CodDisciplina, Nome, _),
        \+ matriculado(_, CodDisciplina, _)
    ), Disciplinas).

% regra  para professores_disciplina
professores_disciplina(CodDisciplina, Professores) :-
    findall(Nome, (
        leciona(IdProf, CodDisciplina),
        professor(IdProf, Nome, _, _, _)
    ), Professores).

% regra para Disciplinas com mais alunos
disciplinas_mais_alunos(Disciplina) :-
    findall(
        (NumAlunos, Nome),
        (
            disciplina(CodDisciplina, Nome, _),
            findall(Aluno, matriculado(Aluno, CodDisciplina, _), ListaAlunos),
            length(ListaAlunos, NumAlunos)
        ),
        Ranking
    ),
    max_member((_,Disciplina), Ranking).

% regra para alunos rprovados (nota < 10)
alunos_reprovados(Reprovados) :-
    findall(Nome, (
        aluno(IdAluno, Nome, _, _, _),
        matriculado(IdAluno, _, nota(Nota)),
        Nota < 10
    ), Reprovados).
