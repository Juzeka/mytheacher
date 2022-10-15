import { Button } from "@mui/material"
import { Professor } from "../../@types/professor"
import { Descricao, Foto, Informacoes, ItemLista, ListasTyled, ListaVazia, Nome, Valor } from "./Lista.style"


interface ListaProps {
    professores: Professor[],
}

const Lista = (props: ListaProps) => {
    return (
        <div>
            {props.professores.length > 0 ? (
                <ListasTyled>
                {props.professores.map(professor => (
                    <ItemLista key={professor.id}>
                        <Foto src={professor.foto}/>
                        <Informacoes>
                            <Nome>{professor.nome}</Nome>
                            <Valor>{professor.valor_hora.toLocaleString('pt-BR', { minimumFractionDigits: 2, style: 'currency', currency: 'BRL' })} por hora</Valor>
                            <Descricao>{professor.descricao}</Descricao>
                            <Button sx={{ width: '70%' }}>Marcar Aula com {professor.nome}</Button>
                        </Informacoes>
                    </ItemLista>
                ))}
            </ListasTyled>
            ) : (
                <ListaVazia>Nenhum professor encontrado!</ListaVazia>
            )}
        </div>
    )
}

export default Lista