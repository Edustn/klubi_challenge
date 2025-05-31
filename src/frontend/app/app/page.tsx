import ChatBot from '../components/ChatBot'

export default function HomePage() {
  return (
    <main className="p-4">
      <h1 className="text-2xl font-bold mb-6 ">Bem-vindo à Klubi</h1>
      <ChatBot />
    </main>
  );
}
