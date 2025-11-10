export default function Card({ children }) {
  return (
    <div
      style={{
        border: '2px solid #ccc',
        borderRadius: '12px',
        padding: '20px',
        marginTop: '20px',
        width: '300px'
      }}
    >
      {children}
    </div>
  )
}


export default function Button({ onClick, text }) {
  return (
    <button
      onClick={onClick}
      style={{
        backgroundColor: '#0a0a44',
        color: 'white',
        border: 'none',
        padding: '10px 20px',
        borderRadius: '8px',
        cursor: 'pointer',
        marginTop: '10px'
      }}
    >
      {text}
    </button>
  )
}
