import ChatBot from '../components/ChatBot';
import Image from 'next/image';
import klubi from '../public/klubi.png'

export default function HomePage() {
  return (
    <main className="bg-[#FFEFD5] p-4 min-h-screen flex flex-col items-center">
      <div className="flex items-center justify-center mb-6 w-full">
        <div className="mr-4">
          <Image src={klubi} alt="Logo do Klubi" width={80} height={80} />
        </div>
        <h1 className="text-2xl font-bold text-zinc-950">Bem-vindo</h1>
      </div>
      <ChatBot />
    </main>
  );
}
