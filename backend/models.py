from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Motorista(Base):
    __tablename__ = "motoristas"

    id = Column(Integer, primary_key = True, index = True, autoincrement = True)
    nome = Column(String, nullable=False)
    cpf = Column(String, nullable=True)
    status = Column(Integer, default=1, nullable=False)

class Vendedor(Base):
    __tablename__ = "vendedores"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, nullable=False)
    loja = Column(String, nullable=True)
    status = Column(Integer, default=1, nullable=False)

class Ajudante(Base):
    __tablename__ = "ajudantes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, nullable=False)
    cpf = Column(String, nullable=True)
    status = Column(Integer, default=1, nullable=False)

class Veiculo(Base):
    __tablename__ = "veiculos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    placa = Column(String, nullable=True)
    marca = Column(String, nullable=True)
    modelo = Column(String, nullable=False)
    ano = Column(Integer, nullable=True)
    status = Column(Integer, default=1, nullable=False)

class Ciclo(Base):
    __tablename__ = "ciclos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, nullable=False)
    data_inicio = Column(String, nullable=True)
    data_fim = Column(String, nullable=True)
    cliente = Column(String, nullable=True)
    observacao = Column(String, nullable=True)
    status = Column(String, nullable=True)

class Pacote(Base):
    __tablename__ = "pacotes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ciclo_id = Column(Integer, ForeignKey("ciclos.id"), nullable=False)
    nome =  Column(String, nullable=False)
    valor = Column(Float, nullable=True)
    observacao = Column(String, nullable=True)

    ciclo = relationship("Ciclo")

class Entrega(Base):
    __tablename__ = "entregas"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ciclo_id = Column(Integer, ForeignKey("ciclos.id"), nullable=True)
    pacote_id = Column(Integer, ForeignKey("pacotes.id"), nullable=True)
    os = Column(String, nullable=True)
    data = Column(String, nullable=False)
    destino = Column(String, nullable=True)
    uf = Column(String, nullable=True)
    veiculo_id = Column(Integer, ForeignKey("veiculos.id"), nullable=True)
    motorista_id = Column(Integer, ForeignKey("motoristas.id"), nullable=True)
    ajudante_id = Column(Integer, ForeignKey("ajudantes.id"), nullable=True)
    vendedor_id = Column(Integer, ForeignKey("vendedores.id"), nullable=True)
    valor = Column(Float, nullable=True)
    peso = Column(Float, nullable=True)
    observacao = Column(String, nullable=True)
    status = Column(String, default="Entregue", nullable=False)

    ciclo = relationship("Ciclo")
    pacote = relationship("Pacote")
    veiculo = relationship("Veiculo")
    motorista = relationship("Motorista")
    ajudante = relationship("Ajudante")
    vendedor = relationship("Vendedor")