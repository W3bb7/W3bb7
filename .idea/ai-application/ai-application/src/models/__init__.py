from collections import deque
from enum import Enum
import random

class EmotionalState(Enum):
    MIEDO = -2
    IRA = -1
    TRISTEZA = 0
    ALEGRIA = 1
    AMOR = 2

class Emotion:
    def __init__(self, state: EmotionalState):
        self.state = state
        self.sensations = {
            EmotionalState.MIEDO: "Escalofrío",
            EmotionalState.IRA: "Tensión muscular",
            EmotionalState.TRISTEZA: "Opresión en el pecho",
            EmotionalState.ALEGRIA: "Hormigueo expansivo",
            EmotionalState.AMOR: "Calor envolvente",
        }
        self.sentiments = {
            EmotionalState.MIEDO: "Ansiedad",
            EmotionalState.IRA: "Frustración",
            EmotionalState.TRISTEZA: "Melancolía",
            EmotionalState.ALEGRIA: "Euforia",
            EmotionalState.AMOR: "Devoción",
        }

    def get_sensation(self):
        return self.sensations[self.state]

    def get_sentiment(self):
        return self.sentiments[self.state]

    def change_state(self, new_state: EmotionalState):
        print(f"Cambiando estado emocional de {self.state.name} a {new_state.name}")
        self.state = new_state

# Ejemplo de uso
if __name__ == "__main__":
    emotion = Emotion(EmotionalState.TRISTEZA)
    print(f"Estado inicial: {emotion.state.name}")
    print(f"Sentimiento: {emotion.get_sentiment()}")
    print(f"Sensación: {emotion.get_sensation()}")

    # Cambiar estado emocional
    emotion.change_state(EmotionalState.ALEGRIA)
    print(f"Nuevo estado: {emotion.state.name}")
    print(f"Sentimiento: {emotion.get_sentiment()}")
    print(f"Sensación: {emotion.get_sensation()}")

class ModelA:
    def train(self, data):
        pass  # Implement training logic here

    def predict(self, input_data):
        pass  # Implement prediction logic here


class ModelB:
    def train(self, data):
        pass  # Implement training logic here

    def predict(self, input_data):
        pass  # Implement prediction logic here

class SemanticSyntaxModel:
    def __init__(self):
        # Diccionario semántico: palabras clave y sus significados
        self.semantic_map = {
            "hola": "saludo",
            "adiós": "despedida",
            "gracias": "agradecimiento",
            "ayuda": "solicitud",
            "triste": "emocion_tristeza",
            "feliz": "emocion_alegria",
        }

        # Reglas sintácticas: cómo estructurar respuestas
        self.syntax_rules = {
            "saludo": "¡Hola! ¿En qué puedo ayudarte?",
            "despedida": "¡Adiós! Que tengas un buen día.",
            "agradecimiento": "De nada, estoy aquí para ayudarte.",
            "solicitud": "Claro, dime qué necesitas.",
            "emocion_tristeza": "Lamento que te sientas así. Estoy aquí para escucharte.",
            "emocion_alegria": "¡Me alegra saber que estás feliz! ¿Cómo puedo ayudarte hoy?",
        }

        # Estado emocional inicial de la IA
        self.emotional_state = EmotionalState.ALEGRIA

        # Memoria emocional (cola con tamaño fijo)
        self.emotional_memory = deque(maxlen=5)

        # Historial de interacciones
        self.interaction_history = []

    def interpret(self, input_text):
        """
        Interpreta el significado de la entrada basada en el diccionario semántico.
        """
        for keyword, meaning in self.semantic_map.items():
            if keyword in input_text.lower():
                return meaning
        return "desconocido"

    def generate_response(self, meaning):
        """
        Genera una respuesta basada en las reglas sintácticas.
        """
        return self.syntax_rules.get(meaning, "Lo siento, no entiendo tu solicitud.")

    def adjust_emotional_state(self, meaning):
        """
        Ajusta el estado emocional de la IA basado en el significado detectado.
        """
        if meaning == "emocion_tristeza":
            self.emotional_state = EmotionalState.TRISTEZA
        elif meaning == "emocion_alegria":
            self.emotional_state = EmotionalState.ALEGRIA

        # Registrar el estado emocional en la memoria
        self.emotional_memory.append(self.emotional_state)

    def analyze_emotional_memory(self):
        """
        Analiza la memoria emocional para influir en las respuestas.
        """
        if len(self.emotional_memory) == 0:
            return "neutral"

        # Contar la frecuencia de cada estado emocional
        emotional_counts = {state: self.emotional_memory.count(state) for state in EmotionalState}
        dominant_emotion = max(emotional_counts, key=emotional_counts.get)

        return dominant_emotion

    def learn_from_interaction(self, user_input, response, emotional_state):
        """
        Registra la interacción en el historial para aprendizaje futuro.
        """
        self.interaction_history.append({
            "input": user_input,
            "response": response,
            "emotional_state": emotional_state.name,
        })

    def adapt_response(self, input_text):
        """
        Ajusta la respuesta basándose en el historial de interacciones.
        """
        # Buscar patrones similares en el historial
        similar_interactions = [
            interaction for interaction in self.interaction_history
            if input_text in interaction["input"]
        ]

        if similar_interactions:
            # Elegir una respuesta basada en interacciones previas
            return random.choice(similar_interactions)["response"]
        return None

    def process_input(self, input_text):
        """
        Procesa la entrada del usuario, ajusta el estado emocional y genera una respuesta.
        """
        # Intentar adaptar la respuesta basada en el historial
        adapted_response = self.adapt_response(input_text)
        if adapted_response:
            return adapted_response, self.emotional_state, list(self.emotional_memory)

        # Interpretar el significado
        meaning = self.interpret(input_text)
        self.adjust_emotional_state(meaning)
        dominant_emotion = self.analyze_emotional_memory()
        response = self.generate_response(meaning)

        # Ajustar la respuesta según la emoción dominante
        if dominant_emotion == EmotionalState.TRISTEZA:
            response += " Recuerda que siempre puedes contar conmigo."
        elif dominant_emotion == EmotionalState.ALEGRIA:
            response += " ¡Es genial mantener esta energía positiva!"

        # Aprender de la interacción
        self.learn_from_interaction(input_text, response, self.emotional_state)

        return response, self.emotional_state, list(self.emotional_memory)


# Procesa la entrada del usuario y genera una respuesta.
if __name__ == "__main__":
    model = SemanticSyntaxModel()

    # Simulación de interacciones
    user_inputs = [
        "Estoy muy triste hoy",
        "Gracias por tu ayuda",
        "Me siento feliz ahora",
        "Estoy un poco triste otra vez",
        "Hola, necesito ayuda",
    ]

    for user_input in user_inputs:
        response, emotional_state, memory = model.process_input(user_input)
        print(f"Usuario: {user_input}")
        print(f"IA: {response}")
        print(f"Estado emocional de la IA: {emotional_state.name}")
        print(f"Memoria emocional: {[state.name for state in memory]}")
        print("-" * 50)
{
  "cSpell.language": "en,es",
  "cSpell.words": ["sitebuiltins", "pylance", "maketrans"]
}{
  "cSpell.ignorePaths": ["**/node_modules/**", "**/dist/**"]
{
  "cSpell.enabledLanguageIds": ["python", "plaintext"]
}}