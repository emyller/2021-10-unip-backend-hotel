create table quartos (
    id serial primary key,
    andar int,
    numero int,
    quantidade_camas int,
    tem_frigobar boolean,
    categoria text
);

create table hospedes (
    id serial primary key,
    nome text,
    endereco text,
    cpf text,
    telefone text,
    email text,
    data_nascimento date
);

create table reserva (
    quarto_id int,
    hospede_id int,
    metodo_pagamento text,
    data_entrada date,
    data_saida date,
    quantidade_pessoas int,
    preco numeric(8, 2),

    foreign key (quarto_id) references quartos (id),
    foreign key (hospede_id) references hospedes (id)
)
