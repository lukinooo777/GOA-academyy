export default function Product({ price, inStock }) {
  return (
    <div style={{ marginBottom: '10px' }}>
      <p>ფასი: {price} ₾</p>
      <p style={{ color: inStock ? 'green' : 'red' }}>
        {inStock ? 'ხელმისაწვდომია ✅' : 'ამოიწურა ❌'}
      </p>
    </div>
  )
}
