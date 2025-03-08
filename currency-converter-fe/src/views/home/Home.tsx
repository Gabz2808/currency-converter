interface HomeProps {}

export const Home: React.FC<HomeProps> = ({}: HomeProps) => {
  return (
    <div className="flex items-center justify-center h-screen">
      <div className="max-w-sm rounded overflow-hidden shadow-lg  text-black font-bold rounded-lg border shadow-lg p-10">
        <div className="font-bold text-xl mb-4 text-center">
          Currency Converter
        </div>
        <div className="flex flex-col space-y-4">
          <select id="origin" className="py-2 px-4 rounded">
            <option>Select Origin</option>
          </select>
          <select id="destiny" className="py-2 px-4 rounded">
            <option>Select Destiny</option>
          </select>
          <input
            type="number"
            id="amount"
            placeholder="Amount"
            className="py-2 px-4 rounded"
          />
          <button className="bg-blue-500 transition delay-150 duration-300 ease-in-out hover:-translate-y-1 hover:scale-110 hover:bg-indigo-500 py-2 px-4 rounded text-white">
            Save Changes
          </button>
          <div className="text-center">
            <p>0</p>
            <div />
          </div>
        </div>
      </div>
    </div>
  );
};
