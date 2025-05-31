'use client';

import { useState } from 'react';

interface Car {
  Name: string;
  Model: string;
  Image: string;
  Price: number;
  Location: string;
}

interface Message {
  sender: 'user' | 'bot';
  text: string;
}

export default function ChatBot() {
  const [messages, setMessages] = useState<Message[]>([
    { sender: 'bot', text: 'Olá! Sou seu assistente da Klubi. Como posso te ajudar hoje?' }
  ]);
  const [input, setInput] = useState('');
  const [car, setCar] = useState<Car | null>(null);
  const [loading, setLoading] = useState(false);

  const handleSend = async () => {
    if (!input.trim()) return;

    const userMessage = { sender: 'user', text: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput('');
    setLoading(true);

    try {
      const res = await fetch('http://localhost:5000/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: input }),
      });

      const data = await res.json();
      setMessages((prev) => [
        ...prev,
        { sender: 'bot', text: data.response }
      ]);

      if (data.cars.length > 0) {
        setCar(data.cars[0]); // Mostra só o primeiro carro relevante
      } else {
        setCar(null);
      }
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        { sender: 'bot', text: 'Desculpe, houve um erro ao processar sua solicitação.' }
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-4 max-w-2xl mx-auto">
      <div className="bg-gray-100 p-4 rounded-lg h-[400px] overflow-y-auto mb-4">
        {messages.map((msg, idx) => (
          <div key={idx} className={`mb-2 ${msg.sender === 'user' ? 'text-right' : 'text-left'}`}>
            <span className={`inline-block px-3 py-2 rounded-lg ${msg.sender === 'user'
                ? 'bg-blue-500 text-white'  // Estilo para mensagens do usuário
                : 'bg-gray-200  text-black'  // Estilo para mensagens do bot (agora com texto preto)
              }`}>
              {msg.text}
            </span>
          </div>
        ))}
        {loading && <p className="text-sm text-gray-500">Pensando...</p>}
      </div>

      <div className="flex gap-2">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Digite sua dúvida sobre carros..."
          className="flex-grow px-4 py-2 border rounded"
        />
        <button onClick={handleSend} className="px-4 py-2 bg-blue-600 text-white rounded">
          Enviar
        </button>
      </div>

      {car && (
        <div className="mt-6 border p-4 rounded-lg shadow">
          <h2 className="text-xl font-semibold mb-2">
            {car.Name} {car.Model}
          </h2>
          <img
            src={`/${car.Image}`} // Ajuste aqui conforme o backend permitir servir imagens
            alt={`${car.Name} ${car.Model}`}
            className="w-full h-48 object-contain mb-2"
          />
          <p>Preço: R$ {car.Price.toLocaleString('pt-BR')}</p>
          <p>Localização: {car.Location}</p>
        </div>
      )}
    </div>
  );
}
