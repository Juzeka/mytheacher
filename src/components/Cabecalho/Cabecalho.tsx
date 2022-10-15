import { CabecalhoContainer, Logo } from "./Cabecalho.style";

const Cabecalho = () => {
    return (
        <div>
          <CabecalhoContainer>
            <div>
              <Logo src='/img/myteacher.png'/>
            </div>
            <p>Encontre o professor perfeito!</p>
          </CabecalhoContainer>
        </div>
    )
}

export default Cabecalho;