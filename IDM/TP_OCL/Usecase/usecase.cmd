!new Diagram('ATM')
!ATM.name := 'ATM'

!new Actor('Client')
!Client.name := 'client'

!new Association('association')
!association.name := 'can'

!new Usecase('Authenticate')
!Authenticate.name := 'authenticate'

!new Usecase('Withraw')
!Withraw.name := 'withdraw'

!new Dependancy('Extend')
!Extend.type := D_Type::Extend

!new Dependancy('Include')
!Include.type := D_Type::Include

!new Usecase('Consult')
!Consult.name := 'Consult Credit'

!insert (ATM,Consult) into DiagramUsecase
!insert (Include,Withraw) into DependacySource
!insert (Include,Authenticate) into DependacyTarget
!insert (Extend,Withraw) into DependacyTarget
!insert (ATM,Authenticate) into DiagramUsecase
!insert (Extend,Consult) into DependacySource
!insert (ATM,Withraw) into DiagramUsecase
!insert (ATM,Client) into DiagramActor
!insert (Withraw,association) into UsecaseAssociation
!insert (Client,association) into ActorAssociation