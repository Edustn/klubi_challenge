'use client';

import { useEffect, useState } from 'react';

interface Car {
  Name: string;
  Model: string;
  Image: string;
  Price: number;
  Location: string;
}

export default function HomePage() {
  const [cars, setCars] = useState<Car[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('/api/cars')
      .then((res) => res.json())
      .then((data) => {
        setCars(data);
        setLoading(false);
      });
  }, []);

  if (loading) return <p className="p-4">Carregando carros...</p>;

  return (
    <main className="p-4">
      <h1 className="text-2xl font-bold mb-4">Lista de Carros</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {cars.map((car, idx) => (
          <div
            key={idx}
            className="border p-4 rounded-lg shadow hover:shadow-md transition"
          >
            <img
              src={`/${car.Image}`}
              alt={`${car.Name} ${car.Model}`}
              className="w-full h-40 object-contain mb-2"
            />
            <h2 className="text-xl font-semibold">
              {car.Name} {car.Model}
            </h2>
            <p>Preço: R$ {car.Price.toLocaleString()}</p>
            <p>Localização: {car.Location}</p>
          </div>
        ))}
      </div>
    </main>
  );
}
