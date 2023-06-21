import Image from 'next/image'
import Link from 'next/link'
import React from 'react'

import Logo from './assets/logo.png'

const Navbar = () => {
  return (
    <div className='flex justify-between align-middle '>
{/* logo */}


        <div><Image src={Logo} /></div>
{/* links */}
<nav className='self-center font-medium text-lg text-[#000a]'>
 <ul className='flex align-middle justify-center  gap-9'>


<li  className='self-center'><Link href={'/'}>Home</Link></li>
<li className='self-center'><Link href={'/'}>About</Link></li>
<li className='self-center'><Link href={'/about'}>Adopt</Link></li>
<li className='self-center'><Link href={'/'}>Our Mission</Link></li>
<li className='self-center'><Link href={'/'}>Support Us</Link></li>
<li className='border-solid border-2 border-green-400  px-8 py-4'><Link href={'/'}>Contact</Link></li>


 </ul>
</nav>

    </div>
  )
}

export default Navbar
