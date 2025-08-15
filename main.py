class ProfissionalSaude:
    """
    Classe base para profissionais de saúde.
    """
    def __init__(self, nome, especialidade):
        self.nome = nome
        self.especialidade = especialidade

    def agendar_consulta(self, paciente, data):
        """Agenda uma consulta para um paciente."""
        print(f"[{self.especialidade}] {self.nome} agendou uma consulta para {paciente} na data {data}")

    def realizar_exame(self, paciente, tipo_exame):
        """Realiza um exame em um paciente."""
        print(f"[{self.especialidade}] {self.nome} fez um exame de {tipo_exame} no paciente {paciente}")


# médico
class Medico(ProfissionalSaude):
    """
    Representa um médico. Herda de ProfissionalSaude.
    """
    def __init__(self, nome, especialidade, crm):
        super().__init__(nome, especialidade)
        self.crm = crm

    def prescrever_medicamento(self, paciente, medicamento):
        """Prescreve um medicamento para um paciente."""
        print(f"[medico - crm {self.crm}] {self.nome} receitou {medicamento} para {paciente}")


# enfermeiro
class Enfermeiro(ProfissionalSaude):
    """
    Representa um enfermeiro. Herda de ProfissionalSaude.
    """
    def __init__(self, nome, especialidade, coren):
        super().__init__(nome, especialidade)
        self.coren = coren

    def aplicar_injecao(self, paciente, medicamento):
        """Aplica uma injeção em um paciente."""
        print(f"[enfermeiro - coren {self.coren}] {self.nome} aplicou {medicamento} em {paciente}")


# testes básicos
print("iniciando sistema da clinica...")
medico_cardio = Medico("dr joao silva", "cardiologia", "crm-sp 123456")
enfermeiro_chefe = Enfermeiro("ana souza", "enfermagem geral", "coren-sp 987654")
print("-" * 40)

# atividades do médico
print("\natividades do medico:")
medico_cardio.agendar_consulta("Carlos Oliveira", "14/08/2025 - 10h00")
medico_cardio.realizar_exame("Carlos Oliveira", "eletrocardiograma")
medico_cardio.prescrever_medicamento("Carlos Oliveira", "atenolol 25mg")
print("-" * 40)

# atividades do enfermeiro
print("\natividades do enfermeiro:")
enfermeiro_chefe.agendar_consulta("Maria Santos", "14/08/2025 - 11h30")  # polimorfismo
enfermeiro_chefe.realizar_exame("Maria Santos", "teste de glicemia")
enfermeiro_chefe.aplicar_injecao("Maria Santos", "vacina da gripe")
print("-" * 40)

# polimorfismo com lista
print("\nrodando lista de funcionarios (polimorfismo)")
equipe_clinica = [medico_cardio, enfermeiro_chefe]
paciente_teste = "Laura Fernandes"
data_teste = "14/08/2025 - 14h00"

for func in equipe_clinica:
    print(f"\nfunc: {func.nome}, esp: {func.especialidade}")  # detalhe rápido
    func.agendar_consulta(paciente_teste, data_teste)
    func.realizar_exame(paciente_teste, "teste de pressão")