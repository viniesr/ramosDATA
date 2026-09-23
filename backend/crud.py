from sqlalchemy.orm import Session
import models
import schemas

def create_motorista(db: Session, motorista: schemas.MotoristaCreate):
    db_motorista = models.Motorista(
        nome=motorista.nome,
        cpf= motorista.cpf,
        status= motorista.status
    )

    db.add(db_motorista)
    db.commit()
    db.refresh(db_motorista)
    return db_motorista

def get_motoristas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Motorista).offset(skip).limit(limit).all()

def get_motorista_by_id(db: Session, motorista_id: int):
    return db.query(models.Motorista).filter(models.Motorista.id == motorista_id).first()

def create_vendedor(db: Session, vendedor: schemas.VendedorCreate):
    db_vendedor = models.Vendedor(
        nome=vendedor.nome,
        loja=vendedor.loja,
        status=vendedor.status
    )

    db.add(db_vendedor)
    db.commit()
    db.refresh(db_vendedor)
    return db_vendedor

def get_vendedores(db: Session, skip: int=0, limit: int=100):
    return db.query(models.Vendedor).offset(skip).limit(limit).all()

def get_vendedor_by_id(db: Session, vendedor_id: int):
    return db.query(models.Vendedor).filter(models.Vendedor.id == vendedor_id).first()

def create_ajudante(db: Session, ajudante: schemas.AjudanteCreate):
    db_ajudante = models.Ajudante(
        nome=ajudante.nome,
        cpf=ajudante.cpf,
        status=ajudante.status
    )

    db.add(db_ajudante)
    db.commit()
    db.refresh(db_ajudante)
    return db_ajudante

def get_ajudantes(db: Session, skip: int=0, limit: int=100):
    return db.query(models.Ajudante).offset(skip).limit(limit).all()

def get_ajudante_by_id(db:Session, ajudante_id: int):
    return db.query(models.Ajudante).filter(models.Ajudante.id == ajudante_id).first()

def create_veiculo(db: Session, veiculo: schemas.VeiculoCreate):
    db_veiculo = models.Veiculo(
        placa=veiculo.placa,
        marca=veiculo.marca,
        modelo=veiculo.modelo,
        ano=veiculo.ano,
        status=veiculo.status
    )

    db.add(db_veiculo)
    db.commit()
    db.refresh(db_veiculo)
    return db_veiculo

def get_veiculos(db: Session, skip: int=0, limit: int=100):
    return db.query(models.Veiculo).offset(skip).limit(limit).all()

def get_veiculo_by_id(db: Session, veiculo_id: int):
    return db.query(models.Veiculo).filter(models.Veiculo.id == veiculo_id).first()

def create_ciclo(db:Session, ciclo: schemas.CicloCreate):
    db_ciclo = models.Ciclo(
        nome=ciclo.nome,
        data_inicio=ciclo.data_inicio,
        data_fim=ciclo.data_fim,
        cliente=ciclo.cliente,
        observacao=ciclo.observacao,
        status=ciclo.status
    )

    db.add(db_ciclo)
    db.commit()
    db.refresh(db_ciclo)
    return db_ciclo

def get_ciclos(db:Session, skip: int=0, limit: int=100):
    return db.query(models.Ciclo).offset(skip).limit(limit).all()

def get_ciclo_by_id(db:Session, ciclo_id: int):
    return db.query(models.Ciclo).filter(models.Ciclo.id == ciclo_id).first()

def create_pacote(db:Session, pacote: schemas.PacoteCreate):
    db_pacote=models.Pacote(
        ciclo_id=pacote.ciclo_id,
        nome=pacote.nome,
        valor=pacote.valor,
        observacao=pacote.observacao
    )

    db.add(db_pacote)
    db.commit()
    db.refresh(db_pacote)
    return db_pacote

def get_pacotes(db:Session, skip: int=0, limit: int=100):
    return db.query(models.Pacote).offset(skip).limit(limit).all()

def get_pacote_by_id(db:Session, pacote_id: int):
    return db.query(models.Pacote).filter(models.Pacote.id == pacote_id).first()

def create_entrega(db:Session, entrega: schemas.EntregaCreate):
    db_entrega=models.Entrega(
        ciclo_id=entrega.ciclo_id,
        pacote_id=entrega.pacote_id,
        os=entrega.os,
        data=entrega.data,
        destino=entrega.destino,
        uf=entrega.uf,
        veiculo_id=entrega.veiculo_id,
        motorista_id=entrega.motorista_id,
        ajudante_id=entrega.ajudante_id,
        vendedor_id=entrega.vendedor_id,
        valor=entrega.valor,
        peso=entrega.peso,
        observacao=entrega.observacao,
        status=entrega.status
    )

    db.add(db_entrega)
    db.commit()
    db.refresh(db_entrega)
    return db_entrega

def get_entregas(db:Session, skip: int=0, limit: int=100):
    return db.query(models.Entrega).offset(skip).limit(limit).all()

def get_entrega_by_id(db:Session, entrega_id: int):
    return db.query(models.Entrega).filter(models.Entrega.id == entrega_id).first()